# -*- coding: utf-8-sig -*-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D


###################################
# Génération des points de contrôle
###################################

# grille cartésienne
n = 4
xmin, xmax = -1., 1.
ymin, ymax = -1., 1.
x = np.linspace(xmin,xmax,n+1)
y = np.linspace(ymin,ymax,n+1)
hx = (xmax-xmin)/n
hy= (ymax-ymin)/n

X,Y = np.meshgrid(x, y)

# points de contrôle suivant une paraboloide hyperbolique
ctrl_pts = X**2 - Y**2

## Affichage de la surface par interpolation linéaire des points de contrôle
# = maillage de contrôle 2D
fig = plt.figure(0)
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, ctrl_pts)
plt.show()


########################
# Surface B-Spline
########################

## B-spline cubique
# !! à compléter
#def BSpline(t) :
#    s =
#    return s

## Affichage de la B-Spline 1D
# !! à compléter

## Grille d'evaluation de la surface B-Spline
rho = 4 # Facteur de subdivision de la grille des points de contrôle
# !! à compléter
#N =  # nombre de points d'évaluation (va de 0 à N)
#surf = np.zeros([N+1,N+1]) # initialisation surface
#xeval =  # abscisse des points d'évaluation
#yeval =  # ordonnée des points d'évaluation


# Creation des points fantômes au bord de la surface
#########################################################

# coordonnée suivant x
# x_ghost=

# coordonnée suivant y
# y_ghost=

# coordonnée suivant z (rangé dans un meshgrid)
ctrl_pts_ghost = np.copy(ctrl_pts)
# ctrl_pts_ghost = 

# Application de la formule (2)
################################

# On applique la formule en mode force brute
# !! à compléter
#for 
#    for 
#       for 
#           for 
                
                
                
########################
# Post-traitement
########################

#xsurf = np.linspace(xmin,xmax,N+1)
#ysurf = np.linspace(ymin,ymax,N+1)
#Xsurf,Ysurf = np.meshgrid(xsurf, ysurf)

# Affichage de la surface par interpolation B-Spline
#fig = plt.figure(2)
#ax = fig.add_subplot(211, projection='3d')
#ax.plot_surface(X, Y, ctrl_pts)
#ax = fig.add_subplot(212, projection='3d')
#ax.plot_surface(Xsurf,Ysurf, surf)
#plt.show()










