#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 09:02:04 2018

@author: alfred_mac
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la
import numpy.fft as fft

L = 6.0

def interpolate(A,freqs,M):
    n = len(freqs)
    p = (0+0j)*np.arange(M) #np.zeros([M,1], dtype='complex')
    x = np.arange(M)*L/M - L/2
    for i in range(M):
        p[i] = 0
        for j in range(n):
            if(j<n/2):
                p[i] += (2*np.pi*1j*j/L)*A[j]*np.exp(2*np.pi*1j*j*x[i]/L)
            elif(j==n/2):
                p[i] += 0*A[j]*(np.exp(2*np.pi*1j*(n/2)*x[i]/L)+np.exp(-2*np.pi*1j*(n/2)*x[i]/L))/2
            else:
                p[i] += (2*np.pi*1j*(j-n)/L)*A[j]*np.exp(2*np.pi*1j*(j-n)*x[i]/L)
            
    p = fft.fftshift(p)
    return (p,x)

ng = 10000
nh = 10000
freqsg = fft.fftfreq(ng, 1.0/L)
freqsg = fft.fftshift(freqsg)

freqsh = fft.fftfreq(nh, 1.0/L)
freqsh = fft.fftshift(freqsh)

g = (1/np.sqrt(2*np.pi))*np.exp(-0.5*freqsg*freqsg)
h = 0.5*np.exp(-abs(freqsh))

gk = fft.fft(g)/ng
hk = fft.fft(h)/nh

dgdx = -(freqsg/np.sqrt(2*np.pi))*np.exp(-0.5*freqsg*freqsg)
dhdx = -(freqsh/abs(freqsh))*0.5*np.exp(-abs(freqsh))

M = np.array([1,2,5,10,20,25,40,50,80,100,125,200,250,400,500,625,1000,2000,5000,10000])
D = np.zeros([len(M),1])

for i in range(len(M)):
    print("Doing for: ",M[i])
#    (Pg,Xg) = interpolate(gk,freqsg,M[i])
    (Ph,Xh) = interpolate(hk,freqsh,M[i])
#    D[i] = max(abs(dgdx[0:ng:int(ng/M[i])]-np.real(Pg)))
    D[i] = max(abs(dhdx[0:nh:int(nh/M[i])]-np.real(Ph)))

plt.semilogx(L/M,D)

#plt.title('Accuracy (or error) vs $\Delta x$ for $g(x)$')
plt.title('Accuracy (or error) vs $\Delta x$ for $h(x)$')
plt.xlabel('$\Delta x$')
plt.ylabel('Accuracy (or error)')
plt.show()
