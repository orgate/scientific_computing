#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 02:44:07 2018

@author: alfred_mac
"""


import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la
import numpy.fft as fft

N = 10000
freqs = fft.fftfreq(N, 1.0/6.0)
freqs = fft.fftshift(freqs)

g = (1/np.sqrt(2*np.pi))*np.exp(-0.5*freqs*freqs)
h = 0.5*np.exp(-abs(freqs))

gk = fft.fft(g)
hk = fft.fft(h)

gk = fft.fftshift(gk)
hk = fft.fftshift(hk)
k = np.arange(N)-N/2
#plt.plot(freqs,g)
#plt.plot(freqs,h)

n=20
plt.plot(k[5000-n:5000+n+1],np.real(gk[5000-n:5000+n+1]))
plt.plot(k[5000-n:5000+n+1],np.real(hk[5000-n:5000+n+1]),'--')

#plt.title('$g(x)=(2\pi)^{-0.5}e^{-0.5x^{2}}$ and $h(x)=0.5e^{-|x|}$')
plt.title('$G(k)=DFT[g(x)]$ and $H(k)=DFT[h(x)]$')
#plt.legend(['$g(x)$','$h(x)$'],loc='upper right')
plt.legend(['$G(k)$','$H(k)$'],loc='upper right')
#plt.xlabel('$x$')
plt.xlabel('$k$')
#plt.ylabel('$g(x)$ or h(x)')
plt.ylabel('$G(k)$ or H(k)')
plt.show()
