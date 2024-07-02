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
def BSpline(t) :
    s = (t >= -2)*(t < -1)*( (t+2)**3/6 ) \
      + (t >= -1)*(t <  0)*( (t+2)**3/6 -4*(t+1)**3/6 ) \
      + (t >=  0)*(t <  1)*( (t+2)**3/6 -4*(t+1)**3/6 + t**3 ) \
      + (t >=  1)*(t <= 2)*( (t+2)**3/6 -4*(t+1)**3/6 + t**3 -4*(t-1)**3/6 )
    return s

## Affichage de la B-Spline 1D
tx= np.linspace(-2.5,2.5,200)
sx = BSpline(tx)
plt.figure(1)
plt.plot(tx,sx)
plt.title("B-Spline 1D")
plt.grid()
plt.show()

## Grille d'evaluation de la surface B-Spline
rho = 2 # Facteur de subdivision de la grille des points de contrôle
N = rho*n # nombre de points d'évaluation (va de 0 à N)
surf = np.zeros([N+1,N+1]) # initialisation surface
xeval = np.linspace(xmin,xmax,N+1) # abscisse des points d'évaluation
yeval = np.linspace(ymin,ymax,N+1) # ordonnée des points d'évaluation


# Creation des points fantômes au bord de la surface
#########################################################

# coordonnée suivant x
x_ghost=np.r_[x[0]-hx,x,x[-1]+hx]

# coordonnée suivant y
y_ghost=np.r_[y[0]-hy,y,y[-1]+hy]

# coordonnée suivant z (rangé dans un meshgrid)
ctrl_pts_ghost = np.copy(ctrl_pts)
ctrl_pts_ghost = np.r_[ [2*ctrl_pts_ghost[0,:]-ctrl_pts_ghost[1,:]], ctrl_pts_ghost, [2*ctrl_pts_ghost[-1,:]-ctrl_pts_ghost[-2,:]]]
ctrl_pts_ghost = np.c_[ 2*ctrl_pts_ghost[:,0]-ctrl_pts_ghost[:,1], ctrl_pts_ghost, 2*ctrl_pts_ghost[:,-1]-ctrl_pts_ghost[:,-2]]

# Application de la formule (2)
################################

# On applique la formule en mode force brute
# Boucle sur les points d'interpolation
for i in range(N+1) :
    for j in range(N+1) :
        # Boucle sur les points de controle pour faire la somme des B_x*B_y (Attention aux indices pour les points fantômes !)
        for ii in range(n+3) :
            for jj in range(n+3) :
                xij,yij = (xeval[i]-x_ghost[ii])/hx,(yeval[j]-y_ghost[jj])/hy
                surf[i,j] += ctrl_pts_ghost[ii,jj]*BSpline(xij)*BSpline(yij)
                
               
########################
# Post-traitement
########################

xsurf = np.linspace(xmin,xmax,N+1)
ysurf = np.linspace(ymin,ymax,N+1)
Xsurf,Ysurf = np.meshgrid(xsurf, ysurf)

# Affichage de la surface par interpolation B-Spline
fig = plt.figure(2)
ax = fig.add_subplot(211, projection='3d')
ax.plot_surface(X, Y, ctrl_pts)
ax = fig.add_subplot(212, projection='3d')
ax.plot_surface(Xsurf,Ysurf, surf)
plt.show()










