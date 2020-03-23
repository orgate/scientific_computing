#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 19:55:30 2018

@author: alfred_mac
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la
import numpy.random as rand
import pFit
import pEval

d = 100
x = 2*rand.random(d)-1

# Test 1 - Function is 1/(1+x)
f = 1/(1+x)
p = pFit.pFit(x,f)
fp = pEval.pEval(x,p)

# Test 2 - Function is e^x
f = np.exp(x)
p = pFit.pFit(x,f)
fp = pEval.pEval(x,p)

# Test 3 - Function is tan(x^3)
f = np.tan(x**3)
p = pFit.pFit(x,f)
fp = pEval.pEval(x,p)

# Test 4 - Function is 3(x^2)/(1+sin(x))
f = 3*x*x/(1+np.sin(x))
p = pFit.pFit(x,f)
fp = pEval.pEval(x,p)

plt.plot(x,f,'b .')
plt.plot(x,fp,'r +')
plt.title('Test 4 - $f(x)=3x^{2}/(1+sin(x))$ and its $f_{p}(x)$ vs $x$')
plt.legend(['$f(x)$','$f_{p}(x)$'])
plt.xlabel('x')
plt.ylabel('$f(x)$ and $f_{p}(x)$')
plt.show()