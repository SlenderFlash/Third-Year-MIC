# -*- coding: utf-8-sig -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


#################
# Image de depart
#################

## Lecture de l'image --> numpy.ndarray(64,64,3)
img = mpimg.imread('sample.jpg')

## Image en nuances de gris
img = np.mean(img,axis=2)

## paramètres de la grille associé à l'image de départ
n = np.shape(img)[0]-1 # n+1 = nombre de pixels de l'image initiale dans chaque direction
x = np.arange(0,n+1)# abscisse pixels image
y = np.arange(0,n+1)# ordonnées pixels image
hx = 1.# taille d'un pixel en x
hy = 1.# taille d'un pixel en y



## Affichage de l'image initiale
plt.figure(0)
plt.imshow(img,cmap='gray')
plt.show()


########################
# Image B-Spline
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
plt.show()

## Grille de l'image sur-echantillonnée
rho = 2 # Facteur de sur-échantillonnage
N = rho*n # nombre de nouveaux pixels (va de 0 à N)
imgRSZ = np.zeros([N+1,N+1]) # initialisation image sur-échantillonnée
xeval = np.linspace(x[0],x[-1],N+1) # abscisse des points d'évaluation
yeval = np.linspace(y[0],y[-1],N+1) # ordonnée des points d'évaluation

# Creation des points fantômes au bord de l'image
#########################################################

# coordonnée suivant x
x_ghost=np.r_[x[0]-hx,x,x[-1]+hx]

# coordonnée suivant y
y_ghost=np.r_[y[0]-hy,y,y[-1]+hy]

# coordonnée suivant z (rangé dans un meshgrid)
img_ghost = np.copy(img)
img_ghost = np.r_[ [2*img_ghost[0,:]-img_ghost[1,:]], img_ghost, [2*img_ghost[-1,:]-img_ghost[-2,:]]]
img_ghost = np.c_[ 2*img_ghost[:,0]-img_ghost[:,1], img_ghost, 2*img_ghost[:,-1]-img_ghost[:,-2]]


# Application de la formule (2)
################################

# On applique la formule en mode intelligent !!
# Boucle sur les points d'interpolation
for i in range(N+1) :
    for j in range(N+1) :
        # Boucle sur les points de controle pour faire la somme des B_x*B_y (Attention aux indices pour les points fantômes !)
        # # On retient les points { np.floor(float(i)/rho))-1 .. int(np.ceil(float(i)/rho))+1) }
        for ii in range(int(np.floor(float(i)/rho))-1,int(np.ceil(float(i)/rho))+2) :
            for jj in range(int(np.floor(float(j)/rho))-1,int(np.ceil(float(j)/rho))+2) :
                xij,yij = (xeval[i]-x_ghost[ii+1])/hx,(yeval[j]-y_ghost[jj+1])/hy
                imgRSZ[i,j] += img_ghost[ii+1,jj+1]*BSpline(xij)*BSpline(yij)


# Affichage de la surface par interpolation B-Spline
fig = plt.figure(2)
ax = fig.add_subplot(211)
ax.imshow(img,cmap='gray')
ax = fig.add_subplot(221)
ax.imshow(imgRSZ,cmap='gray')
plt.show()



