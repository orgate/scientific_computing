#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 03:24:57 2018

@author: alfred_mac
"""
import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la

def DFT(f):
    N = len(f)
    F = (0+0j)*np.arange(N)
    for i in range(N):
        for j in range(N):
            F[i]+= (1/N)*f[j]*np.exp(-2*np.pi*1j*i*j/N)
    
    return F

def iDFT(F):
    N = len(F)
    f = (0+0j)*np.arange(N)
    for i in range(N):
        for j in range(N):
            f[i]+= F[j]*np.exp(2*np.pi*1j*i*j/N)
    
    return f
