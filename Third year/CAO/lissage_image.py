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
#n =  # n+1 = nombre de pixels de l'image initiale dans chaque direction
#x = # abscisse pixels image
#y = # ordonnées pixels image
#hx = # taille d'un pixel en x
#hy = # taille d'un pixel en y



## Affichage de l'image initiale
plt.figure(0)
plt.imshow(img,cmap='gray')
plt.show()


########################
# Image B-Spline
########################

## B-spline cubique
#def BSpline(t) :
#    return s

## Affichage de la B-Spline 1D


## Grille de l'image sur-echantillonnée
rho = 2 # Facteur de sur-échantillonnage
#N =  # nombre de nouveaux pixels (va de 0 à N)
#imgRSZ =  # initialisation image sur-échantillonnée
#xeval =  # abscisse des points d'évaluation
#yeval =  # ordonnée des points d'évaluation

# Creation des points fantômes au bord de l'image
#########################################################

# coordonnée suivant x
# x_ghost=

# coordonnée suivant y
# y_ghost=

# coordonnée suivant z (rangé dans un meshgrid)
img_ghost = np.copy(img)
#img_ghost = 

# Application de la formule (2)
################################

# On applique la formule en mode intelligent !!
# !! à compléter



# Affichage de la surface par interpolation B-Spline
#fig = plt.figure(2)
#ax = fig.add_subplot(211)
#ax.imshow(img,cmap='gray')
#ax = fig.add_subplot(221)
#ax.imshow(imgRSZ,cmap='gray')
#plt.show()



