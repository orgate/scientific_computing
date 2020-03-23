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
#    ...
#    I += c*dx*f.f(x)            # evaluate f at the point x
#    ...
    return f.f(a)                    # estimate of the integral



print("Solution is ",PanelIntegrator(5,2,3))

