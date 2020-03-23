#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 11:26:04 2018

@author: alfred_mac
"""

import numpy as np
import scipy.linalg as sla
import matplotlib.pyplot as plt

N = 100

A = np.array([[0,1],[-1,0]])

t = np.linspace(0,7,N)

S11 = np.zeros(N)
S12 = np.zeros(N)
S21 = np.zeros(N)
S22 = np.zeros(N)

for i in range(N):
    S = sla.expm(t[i]*A)
        
    S11[i] = S[0][0]
    S12[i] = S[0][1]
    S21[i] = S[1][0]
    S22[i] = S[1][1]


plt.plot(t,S11, 'r o')
plt.plot(t,S12)
plt.plot(t,S21)
plt.plot(t,S22, 'g--')
plt.legend(['$S_{11}(t)$','$S_{12}(t)$','$S_{21}(t)$','$S_{22}(t)$'])
plt.xlabel('t')
plt.ylabel('$S_{ij}(t)$')
plt.show()
