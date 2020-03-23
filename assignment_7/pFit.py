#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 19:06:25 2018

@author: alfred_mac
"""

import numpy as np
import numpy.linalg as la

def pFit(X,f):
    V = VanderMonde(X)
    p = la.solve(V,f)
    return p
    
def VanderMonde(X):
    d = len(X)
    VM = np.zeros([d,d])
    for i in range(d):
        for j in range(d):
            VM[i][j] = X[i]**j
            
    return VM