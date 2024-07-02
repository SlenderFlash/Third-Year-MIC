#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Séparation de phase

import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft

import scipy.io.wavfile as wv #librairie pour la manipulation des fichiers .wav

def calc_hanning(m,n):
    return .5*(1 - np.cos(2*np.pi*np.linspace(1,m,m)/(n+1))) 

def hanning(n):
    if (n%2) == 0:
        # Even length window
        half = n//2
        w = calc_hanning(half,n)
        w = np.concatenate((w,w[::-1]))
    else:
        # Odd length window
        half = (n+1)//2
        w = calc_hanning(half,n)
        z=w[::-1]
        w = np.concatenate((w,z[1:]))
    return w

def Analyse(S,N):
    NS=S.shape[0]
    Nf=8*NS//N-7
    Spec=np.zeros((N,Nf))
    Phase=np.zeros((N,Nf))
    H=hanning(N);
    for i in range(Nf):
        temp=H*S[i*N//8:(i+8)*N//8]
        ftemp=fft.fft(temp)
        Spec[:,i]=np.abs(ftemp)
        Phase[:,i]=np.angle(ftemp)
    return Spec,Phase

def Synthese(Spec,Phase):
    N=Spec.shape[0]
    Nf=Spec.shape[1]
    Srec=np.zeros((Nf+7)*N//8)
    H=hanning(N)
    for k in range(Nf):
        ftemp=Spec[:,k]*np.exp(1j*Phase[:,k])
        temp=np.real(fft.ifft(ftemp))
        Srec[k*N//8:(k+8)*N//8]=Srec[k*N//8:(k+8)*N//8]+H*temp
    Srec=Srec/4
    return Srec


Fs11, Smix11=wv.read('Mix11.wav')
Fs21, Smix21=wv.read('Mix21.wav')

#Analyse du premier signal

Spec11, Phase11=Analyse(Smix11,2000)
F=np.fft.fftfreq(2000,1./Fs11)
Nf=Spec11.shape[1]
t=(2000+(2000/8)*np.arange(Nf))/Fs11
X,Y=np.meshgrid(t,F)
Z11=Spec11
CS11=plt.contourf(X,Y,Z11)
cbar11=plt.colorbar(CS11)

plt.xlabel('temps')
plt.ylabel('frequence')
plt.title('Diagramme temps frequence')
plt.show()

#Analyse du second signal

Spec21, Phase21=Analyse(Smix21,2000)
F=np.fft.fftfreq(2000,1./Fs21)
Nf=Spec21.shape[1]
t=(2000+(2000/8)*np.arange(Nf))/Fs21
X,Y=np.meshgrid(t,F)
Z21=Spec21
CS21=plt.contourf(X,Y,Z21)
cbar21=plt.colorbar(CS21)

plt.xlabel('temps')
plt.ylabel('frequence')
plt.title('Diagramme temps frequence')
plt.show()

#Definition de la fonction de séparation

def Separation(Spec1,Spec2,T):
    N=Spec1.shape[0]
    Nf=Spec1.shape[1]
    Spec3=np.zeros((N,Nf))
    Spec4=np.zeros((N,Nf))
    for i in range(800):
        for j in range(Nf):
            if Spec1[i,j]>T*Spec2[i,j]:
                Spec3[i,j]=Spec1[i,j]
                Spec3[N-i-1,j]=Spec1[N-i-1,j]
            else:
                Spec4[i,j]=Spec2[i,j]
                Spec4[N-i-1,j]=Spec2[N-i-1,j]
    return Spec3,Spec4  

Spec2,Spec1=Separation(Spec11,Spec21,1)

Srec1=Synthese(Spec1,Phase21)
Srec2=Synthese(Spec2,Phase11)

wv.write("Essai-S1.wav", Fs21, Srec1/5)
wv.write("Essai-S2.wav", Fs21, Srec2/5)

