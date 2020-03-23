#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 17:00:23 2018

@author: alfred_mac
"""


import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la
import numpy.random as rand
import rFit

D = [10,100,1000]
L = [0.002,0.02,0.2]
CN = np.zeros([len(D),len(L)])

for i in range(len(D)):
    for j in range(len(L)):
        X = 2*rand.random(D[i])-1
        CN[i][j] = la.cond(rFit.matricize(X,L[j]))
        
    

plt.plot(CN)
plt.title('Condition number vs d and L')
plt.legend(['$L=0.002$','$L=0.02$','$L=0.2$','$L=2$'])
plt.xlabel('d')
plt.ylabel('Condition number')
plt.show()
    