#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 07:13:41 2018

@author: alfred_mac
"""


import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la
import numpy.fft as fft
import DirectDFT as SFTW

N=10
f0 = (0+0j)*np.arange(N)
f0 += np.random.random()

f1 = SFTW.DFT(f0)
f2 = SFTW.DFT(f1)
f3 = SFTW.DFT(f2)
f4 = SFTW.DFT(f3)

print("Input f is: ",f0)
print("Applying DFT four times on f gives: ",f4)
diff = sum((f0-100*f4)*np.conj(f0-100*f4))
print("Euclidean norm of difference between f and the result obtained after applying DFT 4 times is:",diff)