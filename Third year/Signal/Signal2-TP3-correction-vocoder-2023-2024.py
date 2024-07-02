#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Vocoder de phase

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

def InterpSpec(Spec,T):
    N=Spec.shape[0]
    Nf2=T.shape[0]
    Spec2=np.zeros((N,Nf2))
    for k in range(Nf2):
        t=T[k]
        indice1=int(np.floor(t))
        alpha=t-indice1
        Spec2[:,k]=(1-alpha)*Spec[:,indice1]+alpha*Spec[:,indice1+1]
    return Spec2

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

def InterpPhase(Phase,T):
    N=Phase.shape[0]
    Nf2=T.shape[0]
    Phase2=np.zeros((N,Nf2))
    t0=T[0]
    indice1=int(np.floor(t0))
    Phase2[:,0]=Phase[:,indice1]
    for k in range(1,Nf2):
        t=T[k]
        indice1=int(np.floor(t))
        dphase=Phase[:,indice1+1]-Phase[:,indice1]
        Phase2[:,k]=Phase2[:,k-1]+dphase
    return Phase2

Fs,S=wv.read('aherohasfallen.wav')
N=2**10 #largeur de la fenêtre
alpha=2 #facteur de compression
Spec,Phase=Analyse(S,N)
Nf=Spec.shape[1]
T=np.arange(0,Nf-3,alpha)
Spec2=InterpSpec(Spec,T)
Phase2=InterpPhase(Phase,T)
Srec=Synthese(Spec2,Phase2)
wv.write("Essai-Vocoder.wav", Fs, Srec)

#ecrire une fonction vocoder prenant en entrée un signal S, 
#sa fréquence associée Fs, la taille du fenêtrage N, le facteur de compression alpha



