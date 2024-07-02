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
# nb de points pour pour tracé
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
# sigma = 

# b. Calcul des sigma''
#==============================

# i. construction systeme lineaire
#-------------------------------------
# on rentre la matrice "diagonal par diagonal" en utilisant un format sparse
# diag_1 =
# diag0 =
# diag1 = 
# A = sp.diags([diag_1, diag0, diag1], [-1, 0, +1], format="csc")
# B = 

# ii. resolution systeme lineaire
#---------------------------------------

# option 1 : solver de python (adapté au format sparse)
# sigma_seconde0 = np.zeros(n+1)
# sigma_seconde0[1:-1] = spl.spsolve(A,B)

# option 2 : méthode du pivot de Gauss
# sigma_seconde1 =

# Vérification
# print ('sigma_seconde0',sigma_seconde0)
# print ('sigma_seconde1',sigma_seconde1)
# sigma_seconde = sigma_seconde1


# c. calcul des sigma'''
# sigma_tierce = 

# d. calcul des sigma'
# sigma_prime =

# 3. Évaluation de la spline d'interpolation
##############################################

# a. évaluation en un point :
#================================= 
# def eval_spline_1pt(xeval1pt,x,sigma,sigma_prime,sigma_seconde,sigma_tierce) :
#    return sigmax

# test : 
# eval à peu près le point milieu
# x_half = (xmin+xmax+0.01)/2
# sigmahalf = eval_spline_1pt(x_half,x,sigma,sigma_prime,sigma_seconde,sigma_tierce)
# eval aux bords
# x_moins = xmin-0.5
# sigmamoins = eval_spline_1pt(x_moins,x,sigma,sigma_prime,sigma_seconde,sigma_tierce)
# x_plus = xmax+0.5
# sigmaplus = eval_spline_1pt(x_plus,x,sigma,sigma_prime,sigma_seconde,sigma_tierce)
# print ('eval ponctuelle en x_moins x_half x_plus',sigmamoins,sigmahalf,sigmaplus)

# b. évaluation en une multitude de points :
#==============================================
# def eval_spline(xeval,x,sigma,sigma_prime,sigma_seconde,sigma_tierce) :
#     return Sigmaxx
    
# test :
# sigmamoins1,sigmahalf1,sigmaplus1 = eval_spline(np.array([x_moins,x_half,x_plus]),x,sigma,sigma_prime,sigma_seconde,sigma_tierce)
# print ('eval globale en x_moins x_half x_plus',sigmamoins1,sigmahalf1,sigmaplus1)

# c. évaluation de la spline aux neval points
#==================================================
# sigma_graphe = 

# 4. Tracé des données et de la spline d'interpolation
#########################################################



# 5. Tracé des dérivées seconde et troisième de la spline (sur [x0,xn])
#########################################################################
