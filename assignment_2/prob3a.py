#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 23:09:06 2018

@author: alfred_mac
"""

from __future__ import unicode_literals
import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True
import matplotlib.pyplot as plt

def PanelIntegrator( n, a, b):  # integrate from a to b with n panels
    dx = (b-a)/n
    import f                    # a module that defines f(x)
    x = np.linspace(a,b,n+1)
    I = sum(dx*f.f(x))            # evaluate f at the point x
    
#    plt.plot(x,f.f(x))
#    plt.show()
    
    return I                    # estimate of the integral



#print("Panel Integral (using simple rectangle rule) is: ",PanelIntegrator(1e2,0,2))
#print("Expected result is: ",1-np.cos(2))

# Convergence study for Panel Integrator
N = 10
INTG = np.linspace(1,2,N)*0
DIFF = INTG*0

for i in range(N):
    INTG[i] = PanelIntegrator(1e1*pow(2,i),0,2)
    DIFF[i] = INTG[i] - 1 + np.cos(2)
    

#print("INTG is ",INTG)
#print("DIFF is ",DIFF)
X = 2/(1e1*pow(2,np.arange(N)))
plt.plot(X,DIFF)

plt.xlabel(r'$\Delta{x}$')
plt.ylabel(r'$\Delta{f}$')

plt.show()
