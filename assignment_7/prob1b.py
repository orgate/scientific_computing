#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:48:28 2018

@author: alfred_mac
"""


import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la
import numpy.random as rand
import pFit
import pEval

D = 30
CN = 0*np.arange(D)

for i in range(D):
    x = 2*rand.random(i+1)-1
    V = pFit.VanderMonde(x)
    CN[i] = la.cond(V)
    
plt.semilogy(np.arange(D)+1,CN)
plt.title('Condition number vs d')
plt.xlabel('d')
plt.ylabel('Condition number')
plt.show()
    