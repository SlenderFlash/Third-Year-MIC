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
#Y = np.array([ 4.8, 4., 4., 8., 8., 9., 30., 39., 56., 68.5, 69., 69., 68.5, 56., 39., 30., 9., 8., 8., 4., 4., 4.8 ])

# courbe paramétrique
#X = np.array([1.9, 10.0, 13.0, 16.0, 19.5, 20., 8.5, 11.0, 12.0, 5.5, 2.0, 1.9 ])
#Y = np.array([9.0, 14.0, 11.0, 7.5, 11.0, 4.0, 5.0, 9.0, 3.0, 1.0, 1.5, 9.0 ])

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
# plt.figure(0)
# !! à compléter
# plt.show()


# Q2. Prologement aux extrémités ("points fantômes")
#####################################################
#courbePeriodique = 0
#if # !! à compléter
     # courbePeriodique  = int(input('Le polygone de controle est fermé. Voulez-vous une courbe "bien" fermée  (non : 0  oui : 1) ?'))
#if courbePeriodique == 1 :  # prolongement "périodique"
     # !! à compléter
#else :                      # prolongement "spline naturelle"
     # !! à compléter
     
     
# Q3. Calcul des valeurs aux noeuds des deux approximations B-spline (en X et en Y)
####################################################################################
# !! attention aux points fantômes rajoutés qui agrandissent les vecteurs X et Y
# sigma_x = 
# sigmaPrime_x = 
# sigmaSeconde_x = 
# sigmaTierce_x = 

# sigma_y = 
# sigma"Prime_y = 
# sigmaSeconde_y = 
# sigmaTierce_y = 


# Q4. Calcul de la courbe B-Spline aux points de tracé
##########################################################

# On importe la routine d'évaluation d'une spline en une multitude de points (cf. TP1)
    
# On evalue les deux approxiamtions B-spline
# X_graphe = 
# Y_graphe = 


# Q5. Tracé de la courbe B-spline
##################################
# courbe avec points de controle (et points fantômes)
#plt.figure(1)
#plt.show()

# courbe avec points de controle (sans points fantômes)
#plt.figure(2)
#plt.show()

# courbe avec approx B-spline en x et y
#plt.figure(3)
#plt.show()

# Q6. Modification des courbes en temps reel (par click sur graphique)
########################################################################
# import PlotSplineModifiable as pm
# imagemodifiable = pm.DrawModifiableSpline(X,Y,courbePeriodique,courbeBSpline)









