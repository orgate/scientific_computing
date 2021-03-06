#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 12:14:01 2018

@author: alfred_mac
"""

import numpy as np
import matplotlib.pyplot as plt

e = 0.5         # eccentricity
M = 0.2         # mean anomaly
E_1 = 0.0       # initial value for E(-1)
E0 = 1.0        # initial value for E(0)
E = [E_1,E0]    # list of E's (values of eccentric anomaly)

def flinear(E_1,E0,e,M,E):
    if(abs(E0-E_1)>1e-10):
        E1 = M + (e*np.sin(E0))
        E.append(E1)
        return flinear(E0,E1,e,M,E)
    
    return E0,E

print("After many iterations, result is:")
print(flinear(E_1,E0,e,M,E))

print(abs(np.array(E[2:-1])-E[-1])/abs(np.array(E[1:-2])-E[-1]))

plt.loglog(abs(np.array(E[1:-1])-E[-1]),abs(np.array(E[2:])-E[-1]))
plt.title('Linear Method')
plt.xlabel('$log|E_{n}-E^{*}|$')
plt.ylabel('$log|E_{n+1}-E^{*}|$')
plt.show()