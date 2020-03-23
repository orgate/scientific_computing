#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 06:05:48 2018

@author: alfred_mac
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la
import numpy.fft as fft
import DirectDFT as SFTW

N=10
fi = np.random.random([N,1])
gi = np.zeros([N,1])

gi[1:] = fi[0:-1]
gi[0] = fi[-1]

fo = SFTW.DFT(fi)
go = SFTW.DFT(gi)

go_est = fo*0

for i in range(N):
    go_est[i] = fo[i]*np.exp(-2*np.pi*1j*i/N)
    
    
print("go is: ",go)
print("go_est is: ",go_est)
diff = sum(abs(go-go_est))
print("Absolute difference between the estimated and actual values of DFT of g is:",diff)