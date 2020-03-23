#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 16:21:33 2018

@author: alfred_mac
"""


import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la
import numpy.random as rand
import rFit
import rEval

d = 100
x = 2*rand.random(d)-1
L = 2
'''
# Test 1 - Function is e^(-0.5*x^2)
f = np.exp(-0.5*x*x)
p = rFit.rFit(x,f,L)
fp = rEval.rEval(x,p,L)

# Test 2 - Function is e^x
f = np.exp(x)
p = rFit.rFit(x,f,L)
fp = rEval.rEval(x,p,L)
'''
# Test 3 - Function is tan(x^3)
f = np.tan(x**3)
p = rFit.rFit(x,f,L)
fp = rEval.rEval(x,p,L)

# Test 4 - Function is 3(x^2)/(1+sin(x))
f = 3*x*x/(1+np.sin(x))
p = rFit.rFit(x,f,L)
fp = rEval.rEval(x,p,L)

plt.plot(x,f,'b .')
plt.plot(x,fp,'r +')
plt.title('Test 4 - $f(x)=3x^{2}/(1+sin(x))$ and its $f_{p}(x)$ vs $x$')
plt.legend(['$f(x)$','$f_{p}(x)$'])
plt.xlabel('x')
plt.ylabel('$f(x)$ and $f_{p}(x)$')
plt.show()