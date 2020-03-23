#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 19:50:33 2018

@author: alfred_mac
"""

import numpy as np
import matplotlib.pyplot as plt

# Function definition applying Horner's rule to calculate the series
def expm_alf(t,M,k):
    S = np.eye(len(M)) + (t/k)*M    
    for i in range(k-1):
        S = np.eye(len(M)) + (t/(k-1-i))*np.matmul(M,S)
    return S

# Function to convert a positive integer to a string of digits in base 2 (Source code got from STACK OVERFLOW)
def N_to_base2(n):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n%2))
        n //= 2
    return digits[::-1]

# Function to calculate 2's powers of any matrix to be used for any power of a matrix
def Bs_for_N_to_base2(B,n):
    if n == 0:
        return np.eye(len(B))
    Blist = []
    while n:
        Blist.append(B)
        B = np.matmul(B,B)
        n //= 2
    return Blist[::-1]

# Function calculating any power of a matrix
def B_pow_n(B,digits):
    S = np.eye(2)
    for i in range(len(digits)):
        if digits[i]==1:
            S = np.matmul(S,B[i])
    return S


T = 7                           # Total simulation time
deltat = 0.1                    # delta t used for time step
N = int(T/deltat)               # Total no. of time steps

A = np.array([[0,1],[-1,0]])    # given A

S11 = np.zeros(N)
S12 = np.zeros(N)
S21 = np.zeros(N)
S22 = np.zeros(N)

k=1
S1 = np.eye(2)
S2 = expm_alf(deltat,A,k)
    
# Loop to find which k to use to achieve the required level of accuracy
while(np.max(abs(S1-S2))>1e-10):
    k = k+1
    S1 = S2
    S2 = expm_alf(deltat,A,k)


for i in range(N):        
    i_base2 = N_to_base2(i)
    Sti = B_pow_n(Bs_for_N_to_base2(S2,i), N_to_base2(i))

    # Taking only the real parts as the imaginary parts are insignificant
    S11[i] = np.real(Sti[0][0])
    S12[i] = np.real(Sti[0][1])
    S21[i] = np.real(Sti[1][0])
    S22[i] = np.real(Sti[1][1])

t = np.arange(0,T,deltat)

plt.plot(t,S11, 'r o')
plt.plot(t,S12)
plt.plot(t,S21)
plt.plot(t,S22, 'g--')
plt.legend(['$S_{11}(t)$','$S_{12}(t)$','$S_{21}(t)$','$S_{22}(t)$'])
plt.xlabel('t')
plt.ylabel('$S_{ij}(t)$')
plt.show()
