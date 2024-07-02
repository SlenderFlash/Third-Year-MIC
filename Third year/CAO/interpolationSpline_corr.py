# -*- coding: utf-8-sig -*-
import numpy as np
import numpy.linalg as npl
import scipy.sparse as sp
import scipy.sparse.linalg as spl
import matplotlib.pyplot as plt


# Saisie des points à interpoler

#  Saisie par instruction dans le code
#    (retirer le # pour valider les données proposées ; mettre les données souhaitées)

# x = np.array([1.,2.,3.,4.,4.25,4.5,4.75,5.,6.,7.,8.,9.])
# y = np.array([1.,4.,4.5,2.,2.2,1.6,2.4,2.,4.,6.,7.,7.])
# xmin, xmax = 0.,10.

# x = np.arange(7.)
# y = np.array([ 1./3,2.,2.,4./3,3.,1.,1./3])
# xmin, xmax = -.3, 7.

# x = np.array([1.,2.,3.,4.,5.,6.,7.,8.,9.])
# y = np.array([1.,4.,2.,10.,2.,3.,4.,6.,5.])
# xmin, xmax = 0.,10.

# x = np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.])
# y = np.array([0.,0.,0.,0.,0.,0.,1.,1.,1.,1.,1.,1.])
# xmin, xmax = -1.,12.

# x = np.array([0.,1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.])
# y = np.array([4.,4.,5.,5.6,5.,2.5,.75,-.1,0.,2.7,4.,4.2,4.])
# xmin, xmax = -2., 14.

x = np.array([1.,4.,7.,8.,9.,10.,11.,12.,15.,18.])
y = np.array([1.,3.,7.,6.,7.,6,7.,6.,3.,1.])
xmin, xmax = -1.,20.


# x = np.array([0., 1.5, 2. ,3., 4.5])
# y = np.array([0., -4./3, 1./3, 10./3, 4.])
# xmin, xmax = -1. , 6.


# Q0. Paramètres problème
##########################

# nb de données
n = len(x)-1
# vecteur des h
h = x[1:]-x[:-1]
# nb de points pour tracé
neval = 1201 # 1200 segments


# Q1. Tracer des données
#########################
plt.figure(0)
plt.plot(x,y,'ob')
plt.xlim(xmin,xmax)
plt.ylim(min(y)-1,max(y)+1)
plt.title(u"données à interpoler")
plt.grid()
plt.show()

# Q2. Détermination des 4-uplets de  la spline d'interpolation
#################################################################

# a. calcul des sigma
sigma = y

# b. Calcul des sigma''
#==============================

# i. construction systeme lineaire
# A = np.diag((h[:-1]+h[1:])/3.)+np.diag(h[1:-1]/6.,1)+np.diag(h[1:-1]/6.,-1)
# ou en mode sparse
A = sp.diags([h[1:-1]/6., (h[:-1]+h[1:])/3., h[1:-1]/6.], [-1, 0, +1], format="csc")
B = (sigma[2:]-sigma[1:-1])/h[1:]-(sigma[1:-1]-sigma[:-2])/h[:-1]



# ii. resolution systeme lineaire
#---------------------------------------
sigma_seconde0 = np.zeros(n+1)
sigma_seconde1 = np.zeros(n+1)
# ou si on n'alloue pas qu'avec des 0 au départ, à la fin : s = np.append(0.,s) et s=np.append(s,0)

# option 1 : solver de python
# sigma_seconde0[1:-1] = npl.solve(A,B)
# ou en mode sparse
sigma_seconde0[1:-1] = spl.spsolve(A,B)


# option 2 : méthode du pivot de Gauss
# triangulation
for jj in range(n-2):
    alphajj = A[jj+1,jj]/A[jj,jj] # pivot
    A[jj+1,jj+1] = A[jj+1,jj+1] - alphajj*A[jj,jj+1]
    B[jj+1] = B[jj+1]-alphajj*B[jj]
    
    
# resolution système triangulaire supérieure
sigma_seconde1[n-1]=B[n-2]/A[n-2,n-2]
for jj in range(n-3,-1,-1):
    sigma_seconde1[jj+1] = (B[jj]-A[jj,jj+1]*sigma_seconde1[jj+2])/A[jj,jj]

# Vérification
print ('sigma_seconde0',sigma_seconde0)
print ('sigma_seconde1',sigma_seconde1)
sigma_seconde = sigma_seconde1


# c. calcul des sigma'''
sigma_tierce = np.zeros(n+1)
sigma_tierce[:-1] = (sigma_seconde[1:]-sigma_seconde[:-1])/h

# d. calcul des sigma'
sigma_prime = np.zeros(n+1)
sigma_prime[:-1] = (sigma[1:]-sigma[:-1])/h-h/6*(sigma_seconde[1:]+2*sigma_seconde[:-1])
sigma_prime[-1] = sigma_prime[-2]+h[-1]*sigma_seconde[-2]+(h[-1]**2)/2.*sigma_tierce[-2]

# Q3. Évaluation de la spline d'interpolation
##############################################

# a. évaluation en un point :
#================================= 
def eval_spline_1pt(xeval1pt,x,sigma,sigma_prime,sigma_seconde,sigma_tierce) :
    A,B,C,D,j = sigma[0],sigma_prime[0],0.,0.,-1
    while j<n and xeval1pt >= x[j+1] :
        j = j+1
        A,B,C,D = sigma[j],sigma_prime[j],sigma_seconde[j],sigma_tierce[j]
    hx = xeval1pt-x[max(j,0)]
    sigmax = A+hx*(B+hx*(C/2+hx*D/6))
    return sigmax

# test : 
# eval à peu près le point milieu
x_half = (xmin+xmax+0.01)/2
sigmahalf = eval_spline_1pt(x_half,x,sigma,sigma_prime,sigma_seconde,sigma_tierce)
# eval aux bords
x_moins = xmin-0.5
sigmamoins = eval_spline_1pt(x_moins,x,sigma,sigma_prime,sigma_seconde,sigma_tierce)
x_plus = xmax+0.5
sigmaplus = eval_spline_1pt(x_plus,x,sigma,sigma_prime,sigma_seconde,sigma_tierce)
print ('eval ponctuelle en x_moins x_half x_plus',sigmamoins,sigmahalf,sigmaplus)


# b. évaluation en une multitude de points :
#==============================================
def eval_spline(xeval,x,sigma,sigma_prime,sigma_seconde,sigma_tierce) :
    A,B,C,D,j = sigma[0],sigma_prime[0],0.,0.,-1
    Sigmaxx = []
    for xx in xeval :
        while j<n and xx >= x[j+1] :
            j = j+1
            A,B,C,D = sigma[j],sigma_prime[j],sigma_seconde[j],sigma_tierce[j]
        hxx = xx-x[max(0,j)]
        sigmaxx = A+hxx*(B+hxx*(C/2+hxx*D/6))
        Sigmaxx = Sigmaxx + [sigmaxx]
    Sigmaxx = np.array(Sigmaxx)
    return Sigmaxx
# test :
sigmamoins1,sigmahalf1,sigmaplus1 = eval_spline(np.array([x_moins,x_half,x_plus]),x,sigma,sigma_prime,sigma_seconde,sigma_tierce)
print ('eval globale en x_moins x_half x_plus',sigmamoins1,sigmahalf1,sigmaplus1)

# c. évaluation de la spline aux neval points
#==================================================
x_graphe = np.linspace(xmin,xmax,neval)
sigma_graphe = eval_spline(x_graphe,x,sigma,sigma_prime,sigma_seconde,sigma_tierce)

# 4. Tracé des données et de la spline d'interpolation
########################################################
plt.figure(1)
plt.plot(x,y,'ob',label=u"données")
plt.plot(x_graphe, sigma_graphe,'-r',label="spline d'interpolation")
plt.xlim(xmin,xmax)
plt.title(u"Interpolation de données")
plt.grid()
plt.legend(loc="lower left")
plt.show()

# 5. Tracé des dérivées seconde et troisième de la spline (sur [x0,xn])
#########################################################################
# dérivée seconde : évident car lin par morceaux et C0 en xj

# dérivée troisième : il faut travailler pour afficher du cst par morceaux
xx_der = np.zeros(2*n)
ii = np.arange(len(x)-1)
xx_der[2*ii] = x[:-1]
xx_der[2*ii+1] = x[1:]

sigma_tierce_der = np.zeros(2*n)
sigma_tierce_der[2*ii] = sigma_tierce[:-1]
sigma_tierce_der[2*ii+1] = sigma_tierce[:-1]


plt.figure(2)
plt.plot(x, sigma_seconde,'-o',label=u"derivée seconde")
plt.plot(xx_der, sigma_tierce_der,'-m',label=u"derivée troisième")
plt.xlim(xmin,xmax)
plt.title(u"Interpolation de données")
plt.grid()
plt.legend()
plt.show()
