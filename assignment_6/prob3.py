#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 05:03:40 2018

@author: alfred_mac
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la
import numpy.fft as fft

L = 6.0

def interpolate(A,freqs,M):
    n = len(freqs)
    p = np.zeros([M,1], dtype='complex')
    x = np.arange(M)*L/M - L/2
    for i in range(M):
        p[i] = 0
#        for j in range(n):
#            p[i] += A[j]*np.exp(2*np.pi*1j*j*x[i]/L)
        for j in range(n):
            if(j<n/2):
                p[i] += A[j]*np.exp(2*np.pi*1j*j*x[i]/L)
            elif(j==n/2):
                p[i] += A[j]*(np.exp(2*np.pi*1j*(n/2)*x[i]/L)+np.exp(-2*np.pi*1j*(n/2)*x[i]/L))/2
            else:
                p[i] += A[j]*np.exp(2*np.pi*1j*(j-n)*x[i]/L)

            
    p = fft.fftshift(p)
    return (p,x)

ng = 1000
nh = 1000
M = 1000
freqsg = fft.fftfreq(ng, 1.0/L)
freqsg = fft.fftshift(freqsg)

freqsh = fft.fftfreq(nh, 1.0/L)
freqsh = fft.fftshift(freqsh)

g = (1/np.sqrt(2*np.pi))*np.exp(-0.5*freqsg*freqsg)
h = 0.5*np.exp(-abs(freqsh))

gk = fft.fft(g)/ng
hk = fft.fft(h)/nh

(Pg,Xg) = interpolate(gk,freqsg,M)
(Ph,Xh) = interpolate(hk,freqsh,M)

#plt.plot(freqsg,g)
#plt.plot(Xg,np.real(Pg),'--')

plt.plot(freqsh,h)
plt.plot(Xh,np.real(Ph),'--')

#plt.title('$g(x)$ and its trigonometric interpolation $p_{g}(x)$')
plt.title('$h(x)$ and its trigonometric interpolation $p_{h}(x)$')
#plt.legend(['$g(x)$','$p_{g}(x)$'])
plt.legend(['$h(x)$','$p_{h}(x)$'])
plt.xlabel('$x$')
#plt.ylabel('$g(x)$ or $p_{g}(x)$')
plt.ylabel('$h(x)$ or $p_{h}(x)$')
plt.show()
