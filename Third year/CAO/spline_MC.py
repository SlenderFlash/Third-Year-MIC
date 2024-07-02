# -*- coding: utf-8-sig -*-
import numpy as np
import numpy.linalg as npl
import matplotlib.pyplot as plt


#-----------------------------------------------------#
# Saisie des données à représenter avec spline des MC #
#-----------------------------------------------------#


x = np.array([1., 2., 3., 4., 5., 6., 7., 8., 9. ])
y = np.array([1., 4., 2., 1., 2., 3., 4., 6., 2.])

#x = np.array([1., 2., 3., 4., 5., 6., 7., 8., 9.])
#y = np.array([0., 0., 0., 0., 0., 1., 0., 0., 0.])

#x = np.array([1., 2., 3., 4., 4.25, 4.5, 4.75, 5., 6., 7., 8., 9.])
#y = np.array([1., 4., 4.5, 2., 2.2, 1.6, 2.4, 2., 4., 6., 7., 5.])

# PH métrie : Amoniaque / Acide chloridrique
#x = np.array([2., 4., 6., 8., 10., 12., 14., 16., 18., 18.5, 19., 19.1, 19.17, 19.3, 19.5, 20., 21., 22., 23., 25.])
#y = np.array([10.2, 9.9, 9.6, 9.5, 9.3, 9.1, 8.9, 8.7, 8.1, 7.8, 7.2, 6.3, 5.3, 4., 3.1, 2.6, 2.3, 2.1, 2., 1.9])

# PH métrie : Acide méthanoique / soude
#x = np.array([4., 5., 6., 6.5, 6.7, 7., 7.4, 7.6, 7.8, 8., 8.2, 8.4, 8.6, 8.9, 9.3, 9.5, 10., 10.5, 11., 12., 13.])
#y = np.array([3.7, 3.8, 4., 4.2, 4.3, 4.5, 4.9, 5.3, 6.1, 8.6, 10.1, 10.5, 10.8, 11., 11.3, 11.4, 11.6, 11.8, 11.9, 12., 12.1])




# Q0. Paramètres problème
##########################

# nb de données
N = len(x)-1
# nb de noeuds pour la spline des MC (à eseigner en lien avex le jeu de données...)
n = 4 # !! n+1 noeuds en vrai (pour que l'on parte de 0)
# pour le tracé
xmin, xmax, neval = np.min(x)-1, np.max(x)+1, 1201


# Q1. Tracer des données
#########################
# plt.figure(0)
# !! à compléter
# plt.show()

# Q2. Paramètres de la spline des MC
#####################################
# pas
# H =
# liste des noeuds (composante en X)
# X =


# Q3. Expression de la B-Spline (pas 1, centrée en 0)
########################################################
#def Bspline(xx) :
#   
#    return  yy
    
# Q4. Calcul de la matrice U et du vecteur Y
##############################################
# Allocation mémoire U

# remplissage colonne 2 à n-2 (simple : ici Cj = Bj)



# remplissage colonne 1 et 2 de U (Attention : ici, C0 et C1 modifiées par rapport à B0 et B1)


# remplissage colonne n-1 et n de U (Attention : ici, Cn-1 et Cn modifiées par rapport à Bn-1 et Bn)


# Calcul de Y


# Q5. Resolution des équations normales
########################################
# a = 

# Q6. Calcul de l'approximation B-spline correspondant à la spline des MC
##########################################################################

# ajout des points "fantômes" (mode "naturel" cf. cours)
    
     
# valeur aux noeuds


# On importe la routine d'évaluation d'une spline en une multitude de points (cf. TP1)


# on evalue l'approximation B-spline

# Q7. Tracé des données et de la spline des MC
#########################################################
# plt.figure(1)
# !! À compléter
# plt.show()






