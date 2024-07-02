#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft

#Partie 2: Transformée de Fourier à fenêtre

#Exercice 1 - Analyse d'un signal périodique par morceaux

# #Question 1
# Fe=2400. #fréquence d'échantillonnage
# Te=1./Fe
# F1=400 #fréquence 1
# F2=600 #fréquence 2
# dt1=np.arange(0,2,Te) #grille d'échantillonnage du signal 1
# dt2=np.arange(0,3,Te) #grille d'échantillonnage du signal 2
# s1=np.cos(2*np.pi*F1*dt1) #signal 1
# s2=np.cos(2*np.pi*F2*dt2) #signal 2
# s=np.hstack((s1, s2)) #signal périodique par morceaux
# N=len(s) #taille totale du signal à analyser


#Exercice 2 #fréquence instantanée
#Question 1
Fe=2400. #fréquence d'échantillonnage
Te=1./Fe
#Construction d'un chirp linéaire: la fréquence locale croit linéairement
F1=400
a1=2*np.pi*F1
b1=2*np.pi*F1/5
dtc1=np.arange(0,5,Te) #grille echantillonnage totale
s_chirp1=np.cos(a1*dtc1+b1*dtc1**2) #chirp linéaire
#s=s_chirp1
#N=len(s)
#FeSon=Fe

#Question 2
F2=600
a2=2*np.pi*F2
b2=2*np.pi*F2/40
dtc2=np.arange(0,5,Te) #grille echantillonnage totale
s_chirp2=np.cos(a2*dtc2+b2*dtc2**2) #chirp linéaire
#s=s_chirp1+s_chirp2
#N=len(s)
#FeSon=Fe

#Question 3
F3=200
a3=2*np.pi*F3
b3=5.3
dtc3=np.arange(0,5,Te) #grille echantillonnage totale
s_chirp3=np.cos(a3/(b3-dtc3))
#s=s_chirp3
#N=len(s)
#FeSon=Fe


#Question 4
F4=300
a4=2*np.pi*F4
b4=5.15
dtc4=np.arange(0,5,Te) #grille echantillonnage totale
s_chirp4=np.cos(a4/(b4-dtc4))
s=s_chirp3+s_chirp4
N=len(s)
FeSon=Fe

#Question 5 analyse signal sonore

import scipy.io.wavfile as wv

# Freq, Signal=wv.read('basson.wav')
# Freq, Signal=wv.read('garage.wav')
# Freq, Signal=wv.read('drum.wav')
#Freq, Signal=wv.read('flute.wav')
#FeSon=Freq
#s=Signal
#N=len(s)


#Calcul et visualisation de la transformée de Fourier à fenêtre


#Paramètres de la transformée de Fourier à fenêtre
p=2**6 #demi-largeur de fenêtre
n=int(p/4) #recouvrement temporel
T=2.*p/FeSon #Largeur temporelle de la fenêtre
F=np.arange(p)/T #Vecteur des fréquences observées
#t=[] #vecteur des temps
S=np.zeros(p) #matrice des coefficients de Fourier: 
    #on ne prend que la première moitié des coefficients, le signal étant réel
w=np.hanning(2*p) #déclaration de la fenêtre: fenetre de Hanning
#w=np.hamming(2*p) #

#Calcul du spectrogramme
for k in np.arange(p+1,N-p+1,n+p):
    #t=np.hstack((t,[k/Fe])) #construction du vecteur temps
    xw=w*s[k-p:k+p] #produit de la fenetre avec le signal
    yw=fft.fft(xw)/len(xw) # transformée de Fourier
    S=np.vstack((S,np.abs(yw[:p])))
    
#Représentation du spectrogramme    
t=np.arange(p+1,N-p+1,n+p)/FeSon
X,Y=np.meshgrid(t,F)      
Z=S[1:,]


CS=plt.contourf(X,Y,Z.T,10,cmap=plt.cm.bone)
cbar=plt.colorbar(CS)

plt.xlabel('temps')
plt.ylabel('frequence')
plt.title('Diagramme temps frequence')
plt.show()
