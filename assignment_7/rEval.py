#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 16:18:13 2018

@author: alfred_mac
"""

import numpy as np
import numpy.linalg as la
import rFit

def rEval(X,W,L):
    d = len(W)
    f = np.matmul(rFit.matricize(X,L),W)
        
    return f
    