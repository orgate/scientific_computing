#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 05:34:15 2018

@author: alfred_mac
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la
import numpy.fft as fft
import DirectDFT as SFTW

fi = np.array([0,0,0,0,1,0,0,0,0,0])
fo = SFTW.DFT(fi)

C = sum(fi*np.conj(fi))/sum(fo*np.conj(fo))

print("The value of C for an arrray of 10 elements is: ",C)