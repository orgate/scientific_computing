#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 06:49:54 2018

@author: alfred_mac
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la
import numpy.fft as fft
import DirectDFT as SFTW

N=10
fi = (0+0j)*np.arange(N)
fi += np.random.random()

fo = SFTW.DFT(fi)

fi1 = SFTW.iDFT(fo)

print("Input f is: ",fi)
print("iDFT of DFT of f is: ",fi1)
diff = sum((fi-fi1)*np.conj(fi-fi1))
print("Euclidean norm of difference between f and iDFT of DFT of f is:",diff)