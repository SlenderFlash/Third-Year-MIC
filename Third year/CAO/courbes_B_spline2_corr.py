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
#X = np.array([ 22., 34., 39., 39., 24., 24., 25., 39., 39., 30., 30., 14., 14., 5., 5., 19., 20., 20., 5., 5., 10., 22.])
#Y = np.array([ 4.8, 4., 4., 8., 8., 8., 35., 55., 82., 99., 99., 99., 99., 82., 55., 35., 8., 8., 8., 4., 4., 4.8 ])

# verre
X = np.array([22., 34., 39., 39., 24.8, 25., 27., 42., 42., 34.5, 34., 10., 9.5, 2., 2., 17., 19., 19.2, 5., 5., 10., 22.])
Y = np.array([ 4.8, 4., 4., 8., 8., 9., 30., 39., 56., 68.5, 69., 69., 68.5, 56., 39., 30., 9., 8., 8., 4., 4., 4.8 ])

# courbe paramétrique
#X = np.array([1.9, 10.0, 13.0, 16.0, 19.5, 20., 8.5, 11.0, 12.0, 5.5, 2.0, 1.9 ])
#Y = np.array([9.0, 14.0, 11.0, 7.5, 11.0, 4.0, 5.0, 9.0, 3.0, 1.0, 1.5, 9.0 ])

# aile d'avion
#X = np.array([ 42., 32., 19., 1., 1., 22., 34., 42. ])
#Y = np.array([ 1., 4., 1., 1., 8., 11., 6.5,  1.2])

# carré
#X = np.array([0., 0., 0., 0.5, 1., 1., 1., 0.5, 0.])
#Y = np.array([0., 0.5, 1., 1., 1., 0.5, 0., 0., 0. ])

# test
#X = np.array([1.,1.,0.,0.,0.,1.])
#Y = np.array([1.,0.,0.,0.,1.,1.])
#
#X = np.array([1.,1.,0.,0.,1.])
#Y = np.array([1.,0.,0.,1.,1.])

#X = np.array([0.,0.,1.,1.,0.])
#Y = np.array([0.,1.,1.,0.,0.])

courbePeriodique = 1

# On importe la routine d'évaluation d'une spline en une multitude de points (cf. TP1)
def eval_spline(xeval,x,sigma,sigma_prime,sigma_seconde,sigma_tierce) :
    n = len(x)-1
    j = -1; A = sigma[0]; B = sigma_prime[0]; C = 0; D = 0
    Sigmaxx = np.zeros_like(xeval)
    ieval = 0
    for xeval1pt in xeval:
        while j<n and xeval1pt>=x[j+1]:
            j+=1
            A = sigma[j]
            B = sigma_prime[j]
            C = sigma_seconde[j]/2
            D = sigma_tierce[j]/6
        h = xeval1pt-x[max(0,j)]
        Sigmaxx[ieval] = A + h*(B + h*(C + h*D))
        ieval+=1
    return Sigmaxx



def courbeBSpline(X,Y,courbePeriodique):

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
    
    
    ## Q1. Tracer du maillage de controle
    #########################################
    #plt.figure(0)
    #plt.plot(X,Y,'o:',label='Polygone de controle')
    #plt.title('Polygone de controle')
    #plt.axis('equal')
    #plt.pause(0.1)
    #plt.show()
    
    
    # Q2. Prologement aux extrémités ("points fantômes")
    #####################################################
    #courbePeriodique = 0
    
    ## ATTENTION : penser à mettre "int" sur le "input"
    #if courbePeriodique == 0 : #???
    #     courbePeriodique  = int(input('Le polygone de controle est fermé. Voulez-vous une courbe "bien" fermée  (non : 0  oui : 1) ?'))
    
    if courbePeriodique == 1 :  # prolongement "périodique"
         X = np.r_[X[-2],X,X[1],X[2]]
         Y = np.r_[Y[-2],Y,Y[1],Y[2]]
    else :                      # prolongement "spline naturelle"
         X = np.r_[2*X[0]-X[1],X,2*X[-1]-X[-2],3*X[-1]-2*X[-2]]
         Y = np.r_[2*Y[0]-Y[1],Y,2*Y[-1]-Y[-2],3*Y[-1]-2*Y[-2]]
         
        
    # Q3. Calcul des valeurs aux noeuds des deux approximations B-spline (en X et en Y)
    ####################################################################################
    # !! attention aux points fantômes rajoutés qui agrandissent les vecteurs X et Y
    # X d'indices [-1,0,1,...,n,n+1,n+2] (taille n+4)
    h = 1 # car t = np.arange(0,n+1) : pas de 1
    
    sigma_x = (X[2:-1] + 4*X[1:-2] + X[:-3])/6
    sigmaPrime_x = (X[2:-1] - X[:-3])/(2*h)
    sigmaSeconde_x = (X[2:-1] - 2*X[1:-2] + X[:-3])/h**2
    sigmaTierce_x = (X[3:] - 3*X[2:-1] + 3*X[1:-2] - X[:-3])/h**3
    
    sigma_y = (Y[2:-1] + 4*Y[1:-2] + Y[:-3])/6
    sigmaPrime_y = (Y[2:-1] - Y[:-3])/(2*h)
    sigmaSeconde_y = (Y[2:-1] - 2*Y[1:-2] + Y[:-3])/h**2
    sigmaTierce_y = (Y[3:] - 3*Y[2:-1] + 3*Y[1:-2] - Y[:-3])/h**3
    
    
    # Q4. Calcul de la courbe B-Spline aux points de tracé
    ##########################################################
    
       
    # On evalue les deux approxiamtions B-spline
    t_eval = np.linspace(tgraphe_min,tgraphe_max,neval)
    X_graphe = eval_spline(t_eval,t,sigma_x,sigmaPrime_x,sigmaSeconde_x,sigmaTierce_x)
    Y_graphe = eval_spline(t_eval,t,sigma_y,sigmaPrime_y,sigmaSeconde_y,sigmaTierce_y)
    
    
    ## Q5. Tracé de la courbe B-spline
    ###################################
    ## courbe avec points de controle (et points fantômes)
    #plt.figure(1)
    #plt.plot(X,Y,'o:',label='Polygone de controle et points fantomes')
    #plt.plot(X_graphe,Y_graphe,label='Courbe BS')
    #plt.plot(sigma_x,sigma_y,'x',label='Courbe BS en t')
    #plt.axis('equal')
    #plt.show()
    #plt.legend()
    #plt.title("Courbe avec points de controle (et points fantômes)")
    #
    ## courbe avec points de controle (sans points fantômes)
    #plt.figure(2)
    #plt.plot(X[1:-2],Y[1:-2],'o:',label='Polygone de controle')
    #plt.plot(X_graphe,Y_graphe,label='Courbe BS')
    #plt.plot(sigma_x,sigma_y,'x',label='Courbe BS en t')
    #plt.axis('equal')
    #plt.show()
    #plt.legend()
    #plt.title("Courbe avec points de controle (sans points fantômes)")
    #
    ## courbe avec approx B-spline en x et y
    #plt.figure(3)
    #plt.subplot(211)
    #plt.plot(t,X[1:-2],'o')
    #plt.plot(t_eval,X_graphe)
    #plt.ylabel('x')
    #plt.subplot(212)
    #plt.plot(t,Y[1:-2],'o')
    #plt.plot(t_eval,Y_graphe)
    #plt.ylabel('y')
    #plt.xlabel('t')
    #plt.show()
    #
    
    return X_graphe, Y_graphe



# Q6. Modification des courbes en temps reel (par click sur graphique)
########################################################################
import PlotSplineModifiable as pm
imagemodifiable = pm.DrawModifiableSpline(X,Y,courbePeriodique,courbeBSpline)



