# -*- coding: utf-8-sig -*-
import numpy as np
import matplotlib.pyplot as plt


#---------------------------------------------#
# Saisie des points de controle (X,Y) dans R2 #
#---------------------------------------------#

#  droite
#X=np.linspace(0,31)
#Y=X/2.

# flute
X = np.array([ 22., 34., 39., 39., 24., 24., 25., 39., 39., 30., 30., 14., 14., 5., 5., 19., 20., 20., 5., 5., 10., 22.])
Y = np.array([ 4.8, 4., 4., 8., 8., 8., 35., 55., 82., 99., 99., 99., 99., 82., 55., 35., 8., 8., 8., 4., 4., 4.8 ])

# verre
#X = np.array([22., 34., 39., 39., 24.8, 25., 27., 42., 42., 34.5, 34., 10., 9.5, 2., 2., 17., 19., 19.2, 5., 5., 10., 22.])
# Y = np.array([ 4.8, 4., 4., 8., 8., 9., 30., 39., 56., 68.5, 69., 69., 68.5, 56., 39., 30., 9., 8., 8., 4., 4., 4.8 ])


# courbe paramétrique
# X = np.array([1.9, 10.0, 13.0, 16.0, 19.5, 20., 8.5, 11.0, 12.0, 5.5, 2.0, 1.9 ])
# Y = np.array([9.0, 14.0, 11.0, 7.5, 11.0, 4.0, 5.0, 9.0, 3.0, 1.0, 1.5, 9.0 ])

# aile d'avion
#X = np.array([ 42., 32., 19., 1., 1., 22., 34., 42. ])
#Y = np.array([ 1., 4., 1., 1., 8., 11., 6.5,  1.2])

# carré
#X = np.array([0., 0., 0., 0.5, 1., 1., 1., 0.5, 0.])
#Y = np.array([0., 0.5, 1., 1., 1., 0.5, 0., 0., 0. ])


# Q0. Paramètres problème
##########################

# nb de points de controle
n = len(X)-1
# noeuds en t pour les deux approximations B-splines
t=np.arange(0,n+1)
# on trace pour t allant de [0..n]
tgraphe_min, tgraphe_max = 0, n
# nb de points pour tracé
neval = 2001 # 2000 segments  


# Q1. Tracer du maillage de controle
########################################
plt.figure(0)
plt.plot(X,Y,'-ob')
plt.title(u"maillage de controle")
plt.grid()
plt.show()


# Q2. Prologement aux extrémités ("points fantômes")
#####################################################
courbePeriodique = 0
if X[n]==X[0] and Y[n]==Y[0] :
     courbePeriodique  = input('Le polygone de controle est fermé. Voulez-vous une courbe "bien" fermée  (non : 0  oui : 1) ?')
if courbePeriodique == 1 :  # prolongement "périodique"
     XX = np.zeros(n+4)
     XX[0] = X[n-1]
     XX[1:n+2]=X
     XX[n+2]=X[1]
     XX[n+3] = X[2]
     X = XX
     # ou directement avec concatenate(liste,array)
     # X = np.concatenate(([X[n-1]], X, [X[1]], [X[2]]))
     # Y = np.concatenate(([Y[n-1]], Y, [Y[1]], [Y[2]])) 
     # ou, encore plus simple, avec ravel
     Y = np.r_[Y[n-1], Y, Y[1], Y[2]]
else :                      # prolongement "spline naturelle"
     X = np.concatenate(([2*X[0]-X[1]], X, [2*X[n]-X[n-1]], [3*X[n]-2*X[n-1]]))
     Y = np.concatenate(([2*Y[0]-Y[1]], Y, [2*Y[n]-Y[n-1]], [3*Y[n]-2*Y[n-1]]))
     

   
# Q3. Calcul des valeurs aux noeuds des deux approximations B-spline (en X et en Y)
####################################################################################
# !! attention aux points fantômes rajoutés qui agrandissent les vecteurs X et Y
sigma_x = (X[0:n+1] + 4*X[1:n+2] + X[2:n+3])/6
sigmaPrime_x = (X[2:n+3]-X[0:n+1])/2 ;
sigmaSeconde_x = X[0:n+1] - 2*X[1:n+2] + X[2:n+3] ;
sigmaTierce_x = X[3:n+4] - 3*X[2:n+3] + 3*X[1:n+2] - X[0:n+1] ;

sigma_y = (Y[0:n+1] + 4*Y[1:n+2] + Y[2:n+3])/6 ;
sigmaPrime_y = (Y[2:n+3]-Y[0:n+1])/2 ;
sigmaSeconde_y = Y[0:n+1] - 2*Y[1:n+2] + Y[2:n+3] ;
sigmaTierce_y = Y[3:n+4] - 3*Y[2:n+3] + 3*Y[1:n+2] - Y[0:n+1] ;


# Q4. Calcul de la courbe B-Spline aux points de tracé
##########################################################

# On importe la routine d'évaluaiton d'une spline XWen une multitude de points (cf. TP1)
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
    
# on evalue les deux approxiamtions B-spline
t_graphe = np.linspace(tgraphe_min,tgraphe_max,neval)
X_graphe = eval_spline(t_graphe,t,sigma_x,sigmaPrime_x,sigmaSeconde_x,sigmaTierce_x)
Y_graphe = eval_spline(t_graphe,t,sigma_y,sigmaPrime_y,sigmaSeconde_y,sigmaTierce_y)




# Q5. Tracé de la courbe B-spline
##################################
# courbe avec points de controle (et points fantômes)
plt.figure(1)
plt.plot(X,Y,'-ob',label=u"maillage de controle")
plt.plot(sigma_x,sigma_y,'*m',label=u"points de la spline")
plt.plot(X_graphe, Y_graphe,'-r',label="courbe B-spline")
plt.title(u"Courbe B-spline")
plt.grid()
# plt.legend(loc="lower left")
plt.show()


# courbe avec points de controle (sans points fantômes)
plt.figure(2)
plt.plot(X[1:n+2],Y[1:n+2],'-ob',label=u"maillage de controle")
plt.plot(sigma_x,sigma_y,'*m',label=u"points de la spline")
plt.plot(X_graphe, Y_graphe,'-r',label="courbe B-spline")
plt.title(u"Courbe B-spline")
plt.grid()
# plt.legend(loc="lower left")
plt.show()

# courbe avec approx B-spline en x et y
plt.figure(3)
plt.subplot(311), plt.plot(t,X[1:n+2],'-ob',t_graphe,X_graphe,'-r'), plt.title('x en fonction de t'),plt.grid()
plt.subplot(312), plt.plot(t,Y[1:n+2],'-ob',t_graphe,Y_graphe,'-r'), plt.title('y en fonction de t'),plt.grid()
plt.subplot(313), plt.plot(X[1:n+2],Y[1:n+2],'-ob',X_graphe, Y_graphe,'-r'), plt.title('y en fonction de x'),plt.grid()
plt.show()




