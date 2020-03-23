#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 19:50:33 2018

@author: alfred_mac
"""

import numpy as np

# Function definition applying Horner's rule to calculate the series
def expm_alf(t,M,k):
    S = np.eye(len(M)) + (t/k)*M    
    for i in range(k-1):
        S = np.eye(len(M)) + (t/(k-1-i))*np.matmul(M,S)
    return S

deltat = 0.2                    # delta t used for time step

A = np.array([[0,1],[-1,0]])    # given A

k=1
S1 = np.eye(2)
S2 = expm_alf(deltat,A,k)

# Loop to find which k to use to achieve the required level of accuracy
while(np.max(abs(S1-S2))>1e-10):
    print("When k is",k,'error is ',np.max(abs(S1-S2)))
    k = k+1
    S1 = S2
    S2 = expm_alf(deltat,A,k)
           
print("Finally when k is",k,'error is ',np.max(abs(S1-S2)))
print("S is ",S2)