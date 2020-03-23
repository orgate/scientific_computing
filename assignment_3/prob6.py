#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 15:42:44 2018

@author: alfred_mac
"""
import numpy as np
import random as rnd
import numpy.random as nprnd
import time as t
import matplotlib.pyplot as plt


def matprod_scalar_loop(P,Q):
    
    if len(P.T)==len(Q):
        R = np.zeros([len(P),len(Q.T)])
        for i in range(len(P)):
            for j in range(len(Q.T)):
                for k in range(len(Q)):
                    R[i][j] += P[i][k]*Q[k][j]
                    
    elif len(Q.T)==len(P):
        R = np.zeros([len(Q),len(P.T)])
        for i in range(len(Q)):
            for j in range(len(P.T)):
                for k in range(len(P)):
                    R[i][j] += Q[i][k]*P[k][j]
                    
    else:
        print("Can't multiply theses matrices :(")
        return
    
    return R


def matprod_vector_loop(P,Q):

    if len(P.T)==len(Q):
        R = np.zeros([len(P),len(Q.T)])
        for i in range(len(P)):
            for j in range(len(Q.T)):
                R[i][j] = np.sum(P[i,:]*Q[:,j])
                    
    elif len(Q.T)==len(P):
        R = np.zeros([len(Q),len(P.T)])
        for i in range(len(Q)):
            for j in range(len(P.T)):
                R[i][j] = np.sum(Q[i,:]*P[:,j])
                    
    else:
        print("Can't multiply theses matrices :(")
        return
    
    return R


def matprod_numpy(P,Q):
    return np.matmul(P,Q)


nstart = 10
nend = 300
nstep = 10

N = np.arange(nstart,nend+1,nstep)
T1 = np.zeros(len(N))
T2 = np.zeros(len(N))
T3 = np.zeros(len(N))

for n in range(len(N)):
    A = nprnd.rand(N[n],N[n])
    B = nprnd.rand(N[n],N[n])
    t0 = t.time()
    C = matprod_scalar_loop(A,B)
    t1 = t.time()
    D = matprod_vector_loop(A,B)
    t2 = t.time()
    E = matprod_numpy(A,B)
    t3 = t.time()
    T1[n] = t1-t0
    T2[n] = t2-t1
    T3[n] = t3-t2


plt.plot(N,T1)
plt.plot(N,T2)
plt.plot(N,T3)
plt.legend(['T1','T2','T3'])
plt.xlabel('N')
plt.ylabel('Time taken')
plt.show()

#print("Output is",np.sum(abs(C-D)+abs(D-E)+abs(E-C)))
#print("If the above output is below 1e-3, then maybe the code worked!!")
#print("Time taken for scalar loop matrix multiplication is: ",t1-t0,"seconds")
#print("Time taken for vector loop matrix multiplication is: ",t2-t1,"seconds")
#print("Time taken for matrix multiplication is: ",t3-t2,"seconds")
