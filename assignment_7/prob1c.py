#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 21:04:15 2018

@author: alfred_mac
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la
import numpy.random as rand
import pFit
import pEval

d = 100 # Note: Error increases as d increases too much
x = 4*rand.random(d)-2

# Function is e^(-0.5x^2)
f = np.exp(-0.5*x*x)
p = pFit.pFit(x,f)
fp = pEval.pEval(x,p)


plt.plot(x,f,'b .')
plt.plot(x,fp,'r +')
plt.title('$f(x)=e^{-0.5x^{2}}$ and its $f_{p}(x)$ vs $x$')
plt.legend(['$f(x)$','$f_{p}(x)$'])
plt.xlabel('x')
plt.ylabel('$f(x)$ and $f_{p}(x)$')
plt.show()