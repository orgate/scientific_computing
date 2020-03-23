#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 12:14:01 2018

@author: alfred_mac
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la


Lambda = [1e-3,1e-2,1e-1,1,10,100,1000]
D = [5,20,50,200,500]                     # Different no. of dimensions of the system

def H(X,d,lambda_param):
    N = d
    HX = np.zeros([N,N])
    HX[0,0] = 2 + lambda_param*np.exp(X[0])
    HX[0,1] = -1
    HX[N-1,N-1] = 2 + lambda_param*np.exp(X[N-1])
    HX[N-1,N-2] = -1
    for i in range(N-2):
        HX[i+1,i] = -1
        HX[i+1,i+1] = 2 + lambda_param*np.exp(X[i+1])
        HX[i+1,i+2] = -1
        
    return HX

def G(X,d,lambda_param):
    N = len(X)
    GX = np.zeros([N,1])
    GX[0,0] = (2*X[0]) - X[1] + lambda_param*np.exp(X[0])
    GX[N-1,0] = (2*X[N-1]) - X[N-2] + lambda_param*np.exp(X[N-1])
    for i in range(N-2):
        GX[i+1,0] = (2*X[i+1]) - X[i] - X[i+2] + lambda_param*np.exp(X[i+1])
        
    return GX
    

def Newton_Optimization(X,d,lambda_param):
    Xn = X
    Xn1 = Xn - np.dot(la.inv(H(X,d,lambda_param)),G(X,d,lambda_param))
    if(np.sum((Xn1-Xn)*(Xn1-Xn))>1e-4):
        Xn1 = Newton_Optimization(Xn1,d,lambda_param)
        
    return Xn1

# Loop for simulating different values of Lambda
#for i in range(len(Lambda)):
#    d = 20
#    lambda_param = Lambda[i]
#    X = np.zeros([d,1])
#    RES = Newton_Optimization(X,d,lambda_param)
#    plt.plot(np.arange(d)/d,RES)

# Loop for simulating different values of d
for i in range(len(D)):
    lambda_param = 1
    d = D[i]
    X = np.zeros([d,1])
    RES = Newton_Optimization(X,d,lambda_param)
    plt.plot(np.arange(d)/d,RES)

#plt.title('Varying $\lambda$')
#plt.legend(['$\lambda=0.0001$','$\lambda=0.001$','$\lambda=0.01$','$\lambda=0.1$','$\lambda=1$','$\lambda=10$','$\lambda=100$','$\lambda=1000$'])
plt.title('Varying $d$')
plt.legend(['$d=5$','$d=20$','$d=50$','$d=200$','$d=500$'],loc='lower left')
plt.xlabel('$i$')
plt.ylabel('$X_{i}$')
plt.show()