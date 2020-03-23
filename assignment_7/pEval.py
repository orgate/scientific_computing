#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 19:21:28 2018

@author: alfred_mac
"""

import numpy as np
import numpy.linalg as la

def pEval(x,p):
    d = len(p)
    f = np.zeros(d)#0*np.arange(d)
    for i in range(d):
        f[i] = Horner(x[i],p)
        
    return f
    
def Horner(x,p):
    d = len(p)
    S = 1 + (p[d-1]/p[d-2])*x    
    for i in range(d-2):
        S = 1 + (p[d-2-i]/p[d-3-i])*x*S
    S = p[0]*S  
    return S
