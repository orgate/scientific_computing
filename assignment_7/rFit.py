#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 14:43:09 2018

@author: alfred_mac
"""


import numpy as np
import numpy.linalg as la

def rFit(X,f,L):
    V = matricize(X,L)
    p = la.solve(V,f)
    return p
    
def matricize(X,L):
    d = len(X)
    M = np.zeros([d,d])
    for i in range(d):
        for j in range(d):
            M[i][j] = np.exp(-0.5*(X[i]-X[j])*(X[i]-X[j])/(L*L))
            
    return M