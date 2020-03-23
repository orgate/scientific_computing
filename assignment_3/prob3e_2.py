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

E = sla.eig(A)          # Eigen values and eigen vectors of A
R = E[1]                # R = eigen vectors of A
L = sla.inv(R)          # L = inv(R)
e = E[0]                # Eigen values of A


for i in range(N):
    exp_e = np.diag(np.exp(t[i]*e))     # Exponent of tA
    S = np.matmul(R,np.matmul(exp_e,L)) # Calculating S(t)
        
    # Taking only the real parts as the imaginary parts are insignificant
    S11[i] = np.real(S[0][0])
    S12[i] = np.real(S[0][1])
    S21[i] = np.real(S[1][0])
    S22[i] = np.real(S[1][1])


plt.plot(t,S11, 'r o')
plt.plot(t,S12)
plt.plot(t,S21)
plt.plot(t,S22, 'g--')
plt.legend(['$S_{11}(t)$','$S_{12}(t)$','$S_{21}(t)$','$S_{22}(t)$'])
plt.xlabel('t')
plt.ylabel('$S_{ij}(t)$')
plt.show()
