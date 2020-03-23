#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 03:57:33 2018

@author: alfred_mac
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la
import numpy.fft as fft
import DirectDFT as SFTW

#fi = [0,0,1,0,0,0,0]
#fi = [0,0,0,0,0,1,0]
fi = [0,0,0,0,1,0,0,0,0,0]
fo = SFTW.DFT(fi)

f = open("DFT_output_prob1a.txt","a+")
f.write("Input f is:\n")
np.savetxt(f,fi,fmt='%.2f')

fo_act = (1/N)*np.array(fft.fft(fi))

f.write("Euclidean norm of the difference between the estimated result and the actual result as a measure of accuracy is: ")
f.write(str(sum(abs(fo_act-fo))))
f.write("\n")
f.close()