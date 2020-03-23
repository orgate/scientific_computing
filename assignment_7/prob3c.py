#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 17:27:37 2018

@author: alfred_mac
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la
import numpy.random as rand
import rFit
import rEval

D = [101,1001]
L = [0.002,0.02,0.2,2,20]
Err = np.zeros([len(D),len(L)])

for i in range(len(D)):
    for j in range(len(L)):
        x = 2*rand.random(D[i])-1
        f = np.exp(-0.5*x*x)
        p = rFit.rFit(x,f,L[j])
        fp = rEval.rEval(x,p,L[j])
        Err[i][j] = max(abs(f-fp))

i,j = np.unravel_index(Err.argmin(), Err.shape)
x = 2*rand.random(D[i])-1
f = np.exp(-0.5*x*x)
p = rFit.rFit(x,f,L[j])
fp = rEval.rEval(x,p,L[j])

print("Optimal d is: ",D[i]-1)
print("Optimal L is: ",L[j])

plt.plot(x,f,'b .')
plt.plot(x,fp,'r +')
plt.title('$f(x)=e^{-0.5x^{2}}$ and its $f_{p}(x)$ vs $x$, with optimized d and L')
plt.legend(['$f(x)$','$f_{p}(x)$'])
plt.xlabel('x')
plt.ylabel('$f(x)$ and $f_{p}(x)$')
plt.show()
    