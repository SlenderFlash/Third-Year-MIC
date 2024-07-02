# -*- coding: utf-8-sig -*-
import numpy as np
import numpy.linalg as npl
import scipy.sparse as sp
import scipy.sparse.linalg as spl
import matplotlib.pyplot as plt


# Saisie des points à lisser


#  Saisie par instruction dans le code
#    (retirer le # pour valider les données proposées ; mettre les données souhaitées)

# x = np.array([1.,2.,3.,4.,4.25,4.5,4.75,5.,6.,7.,8.,9.])
# y = np.array([1.,4.,4.5,2.,2.2,1.6,2.4,2.,4.,6.,7.,7.])

# x = np.arange(7.)
# y = np.array([ 1./3,2.,2.,4./3,3.,1.,1./3])

# x = np.array([1.,2.,3.,4.,5.,6.,7.,8.,9.])
# y = np.array([1.,4.,2.,10.,2.,3.,4.,6.,5.])

# PH métrie : Amoniaque / Acide chloridrique
#x = np.array([2., 4., 6., 8., 10., 12., 14., 16., 18., 18.5, 19., 19.1, 19.17, 19.3, 19.5, 20., 21., 22., 23., 25.])
#y = np.array([10.2, 9.9, 9.6, 9.5, 9.3, 9.1, 8.9, 8.7, 8.1, 7.8, 7.2, 6.3, 5.3, 4., 3.1, 2.6, 2.3, 2.1, 2., 1.9])

# PH métrie : Acide méthanoique / soude
#x = np.array([4., 5., 6., 6.5, 6.7, 7., 7.4, 7.6, 7.8, 8., 8.2, 8.4, 8.6, 8.9, 9.3, 9.5, 10., 10.5, 11., 12., 13.])
#y = np.array([3.7, 3.8, 4., 4.2, 4.3, 4.5, 4.9, 5.3, 6.1, 8.6, 10.1, 10.5, 10.8, 11., 11.3, 11.4, 11.6, 11.8, 11.9, 12., 12.1])

# saisie lecture d'un fichier

myfile=open("sub38.dat")
myfile=open("sub41.dat")
myfile=open("technofan.dat")

data=np.loadtxt(myfile)
x = data[:,0]
y = data[:,1]

# fenetre de viualisation
xmin, xmax = min(x)-.5, max(x)+0.5


# Q0. Paramètres problème
##########################

# nb de données
n = len(x)-1
# liste des h
h = x[1:]-x[:-1]
# nb de points pour pour tracé
neval = 1201 # 1200 segments

# force de lissage
rhoGlobal = 1
# poids de chacune des données par rapport aux autres
rhoRelatif = np.ones(len(x))
#exemple : 
# rhoRelatif[4] = 100000
# Au bilan
rho = rhoGlobal*rhoRelatif


# 1. Tracer des données
#########################
plt.figure(0)
plt.plot(x,y,'ob')
plt.xlim(xmin,xmax)
plt.ylim(min(y)-1,max(y)+1)
plt.title(u"données à lisser")
plt.grid()
plt.show()



# 2. Détermination des 4-uplets de  la spline d'ajustement
#################################################################

# a. calcul des sigma''
#==============================

# i. construction systeme lineaire
alphaj = 6./(rho[2:n-1]*h[1:n-2]*h[2:n-1])
betaj = h[1:n-1] - 6.*(h[1:n-1]+h[2:n])/(rho[2:n]*(h[1:n-1]**2)*h[2:n]) - 6.*(h[0:n-2]+h[1:n-1])/(rho[1:n-1]*(h[1:n-1]**2)*h[0:n-2])
gammaj = 2.*(h[0:n-1]+h[1:n])+ 6./(rho[2:n+1]*h[1:n]**2) + 6./(rho[0:n-1]*h[0:n-1]**2) + 6.*((h[0:n-1]+h[1:n])**2)/(rho[1:n]*(h[0:n-1]**2)*h[1:n]**2)
deltaj = betaj
epsj = alphaj
chij =  6.*((y[2:]-y[1:n])/h[1:n]-(y[1:n]-y[:n-1])/h[:n-1])
                
# A = np.diag(alphaj,-2)+np.diag(betaj,-1)+np.diag(gammaj)+np.diag(deltaj,1)+np.diag(epsj,2)
# ou mieux : en mode sparse
A = sp.diags([alphaj, betaj, gammaj, deltaj, epsj ], [-2,-1,0,+1,+2], format="csc")
B = chij

# ii. resolution systeme lineaire
# -> on fait du solveur direct ce coup-ci mais on pourrait recoder Gauss
sigma_seconde = np.zeros(n+1)
# sigma_seconde[1:-1] = npl.solve(A,B)
# ou mieux : en mode sparse
sigma_seconde[1:-1] = spl.spsolve(A,B)


# b. Calcul des sigma'''
#==============================
sigma_tierce = np.zeros(n+1)
sigma_tierce[:-1] = (sigma_seconde[1:]-sigma_seconde[:-1])/h

# c. Calcul des sigma
#==============================
sigma = np.zeros(n+1)
sigma[0] = y[0] - sigma_seconde[1]/(rho[0]*h[0])
sigma[n] = y[n] - sigma_seconde[n-1]/(rho[n]*h[n-1])
sigma[1:n] = y[1:n] - (sigma_seconde[2:]-sigma_seconde[1:n])/(rho[1:n]*h[1:n]) + (sigma_seconde[1:n]-sigma_seconde[:n-1]) / (rho[1:n]*h[:n-1])

# d. calcul des sigma'
#============================
sigma_prime = np.zeros(n+1)
sigma_prime[:-1] = (sigma[1:]-sigma[:-1])/h-h/6*(sigma_seconde[1:]+2*sigma_seconde[:-1])
sigma_prime[-1] = sigma_prime[-2]+h[-1]*sigma_seconde[-2]+(h[-1]**2)/2.*sigma_tierce[-2]

# 3. Évaluation de la spline de lissage
##############################################

# a. évaluation directe en une multitude de points :
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

# b. évaluation de la spline aux neval points
x_graphe = np.linspace(xmin,xmax,neval)
sigma_graphe = eval_spline(x_graphe,x,sigma,sigma_prime,sigma_seconde,sigma_tierce)


# 4. Tracé des données et de la spline d'interpolation
#########################################################
# plt.figure(1)
# plt.plot(x,y,'ob',label=u"données")
# plt.plot(x_graphe, sigma_graphe,'-r',label="spline de lissage")
# plt.xlim(xmin,xmax)
# plt.title(u"lissage de données (rho="+str(rhoGlobal)+")")
# plt.grid()
# plt.legend(loc="lower left")
# plt.show()

# 5. Détermination du "bon" point d'inflexion
###############################################

# initialisation pour stockage mémoire
#------------------------------------------
X_inf = [] # abscisse pt d'inflexion
Y_inf = [] # ordonnee pt d'inflexion
Pente = [] # pente pt d'inflexion
n_inf = 0  # nb pt d'inflexion

# boucle pour trouver les moints d'inflexion
#------------------------------------------------
for i in range(1,n-1):
    if sigma_seconde[i]*sigma_seconde[i+1] < 0.:
        n_inf = n_inf + 1
        x_inf = x[i]-sigma_seconde[i]/sigma_tierce[i]
        hx = x_inf-x[i]
        y_inf = sigma[i] + hx*(sigma_prime[i]+hx*(sigma_seconde[i]/2.+hx*sigma_tierce[i]/6.))
        pente = sigma_prime[i]+hx*(sigma_seconde[i]+hx*sigma_tierce[i]/2.)
        X_inf = X_inf + [x_inf] ; Y_inf = Y_inf + [y_inf] ; Pente = Pente + [pente] 
X_inf = np.array(X_inf) ; Y_inf = np.array(Y_inf) ; Pente = np.array(Pente)

# Recherche du point d'inflexion de pente maximale
#--------------------------------------------------
# indice de l'élément de pente maxi
if n_inf != 0:
    i_pente_max = np.argmax(np.abs(Pente))

# Tracé des données, de la spline et des points d'inflexion (s'ils existent)
#-----------------------------------------------------------------------------
plt.figure(1)
plt.plot(x,y,'ob',label=u"données")
plt.plot(x_graphe, sigma_graphe,'-r',label="spline de lissage")
if n_inf != 0:
    plt.plot(X_inf,Y_inf,'sg',label="pts inflexion")
    plt.plot(X_inf[i_pente_max],Y_inf[i_pente_max],'sm',label="pt inflexion pente maxi")
plt.xlim(xmin,xmax)
plt.title(u"lissage de données (rho="+str(rhoGlobal)+")")
plt.grid()
plt.legend(loc="lower left")
plt.show()



