#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 02:31:29 2018

@author: alfred_mac
"""


from __future__ import unicode_literals
import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True
import matplotlib.pyplot as plt

def PanelIntegrator1( n, a, b):  # integrate from a to b with n panels
    dx = (b-a)/n
    eta = 0.5*np.sqrt(0.6)
    import f                    # a module that defines f(x)
    x = np.linspace(a,b,n+1)
    #Ik = (dx/18.0)*(5.0*f.f(x+(dx/2.0)-(dx*eta))+8.0*f.f(x+(dx/2.0))+5.0*f.f(x+(dx/2.0)+(dx*eta)))# evaluate f at the point x+dx/2 or x{k+0.5} as dx is constant here
    Ik = (dx/6)*(f.f(x)+4*f.f(x+(dx/2.0))+f.f(x+dx))
    I = sum(Ik)
#    plt.plot(x,f.f(x))
#    plt.show()
    
    return I                    # estimate of the integral



#print("Panel Integral1 (using simple rectangle rule) is: ",PanelIntegrator1(1e2,0,2))
#print("Expected result is: ",1-np.cos(2))

# Convergence study for Panel Integrator
N = 20
INTG = np.linspace(1,2,N)*0
DIFF = INTG*0

for i in range(N):
    INTG[i] = PanelIntegrator1(1e1*pow(2.0,i),0.0,2.0)
    DIFF[i] = INTG[i] - 1.0 + np.cos(2.0)
    

#print("INTG is ",INTG)
#print("DIFF is ",DIFF)
X = 2.0/(1e1*pow(2.0,np.arange(N)))
plt.plot(X,DIFF)

#plt.xscale('log')
#plt.yscale('log')

plt.xlabel(r'$\Delta{x}$')
plt.ylabel(r'$\Delta{f}$')

plt.show()
