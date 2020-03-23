#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:51:16 2018

@author: alfred_mac
"""

from __future__ import unicode_literals
import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True
import matplotlib.pyplot as plt

#delta = 1e-7
x = 5                                               # Value of x around which the delta is taken
#x0 = np.arange(delta,2e-4+delta,delta)
xk = pow(2.0,np.arange(-30,2))                      # Taking different values of del x
#xk = x0[1:-1]
#xk1 = x0[2:]
#xkm1 = x0[:-2]
yk = np.exp(x)
yk1 = np.exp(x+xk)
ykm1 = np.exp(x-xk)

ykb = (np.exp(xk/2) - np.exp(-xk/2))*yk/xk
yk1b = (np.exp(xk/2) - np.exp(-xk/2))*yk1/xk
ykm1b = (np.exp(xk/2) - np.exp(-xk/2))*ykm1/xk

diff = ((13/12)*ykb) - ((1/24)*(yk1b+ykm1b)) - yk

#print("x is ",x)
#print("xk is ",xk)

#plt.plot(np.log(xk),np.log(diff))
plt.plot(xk,diff)

plt.xscale('log')
plt.yscale('log')

plt.xlabel(r'$\Delta{x}$')
plt.ylabel(r'$\Delta{f}$')
plt.show()