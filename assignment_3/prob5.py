#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 15:20:58 2018

@author: alfred_mac
"""

import numpy as np
import scipy.linalg as sla
import matplotlib.pyplot as plt


N = 100                 # Time length of the simulation
n = 50                  # Total no. of spots (or the size of X vector)

A = np.zeros([n,n])     # Matrix defining the dynamics
p = 0.7                 # Rate at which particles move left
q = 0.3                 # Rate at which particles move right


# Defining the matrix A
A[0,0] = -p
A[0,1] = p
A[n-1,n-2] = q
A[n-1,n-1] = -q

for i in range(n-2):
    A[i+1,i] = q
    A[i+1,i+1] = -(p+q)
    A[i+1,i+2] = p


t = np.linspace(0,7,N)  # Time counter

X = np.zeros([n,N])     # No. of particles at different spots at different times
X[0,0] = 1              # Initial condition for no. of particles, X

E = sla.eig(A)          # Eigen values and eigen vectors of A
R = E[1]                # R = eigen vectors of A
L = sla.inv(R)          # L = inv(R)
e = np.real(E[0])       # Eigen values of A

AA  = np.eye(n)
for i in range(N-1):
    exp_e = np.diag(np.exp(t[i]*e))     # Exponent of tA
#    AA = np.eye(n)+np.matmul(AA,A)
    S = np.matmul(R,np.matmul(exp_e,L)) # Calculating S(t)
    X[:,i+1] = np.matmul(S,X[:,0])
#    X[:,i+1] = np.matmul(AA,X[:,0])


plt.plot(t,X.T)
#plt.legend(['$x_{1}(t)$'])
plt.xlabel('t')
plt.ylabel('$x_{1}(t)$')
plt.show()

