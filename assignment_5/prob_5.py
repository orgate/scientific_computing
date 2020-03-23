#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 14:07:08 2018

@author: alfred_mac
"""
import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la


def mCh(H):
    N = len(H)
    L = np.zeros([N,N])
    l1 = np.zeros([N,1])
    l2 = np.zeros([N,1])

    # Loop running over each element of L across every column in every row
    for i in range(N):
        if(i==0):
            L[i,i] = np.sqrt(abs(H[i,i]))
        else:
            L[i,i] = np.sqrt(abs(H[i,i]-np.dot((L[i].T),L[i])))
            
        for j in range(N-i-1):
            if(i==0):
                L[j+i+1,i] = H[j+i+1,i]/L[i,i]
            else:
                L[j+i+1,i] = (H[j+i+1,i] - np.dot((L[j+i+1].T),L[i]))/L[i,i]
                
    eig_H = la.eig(H)
    flag = 0
    
    # Loop verifying if the matrix is positive definite by checking if each eigen value is positive
    for i in range(N):
        if(eig_H[0][i]<=0):
            flag = 1
            
    P = True
    if(flag==1):
        P = False

    return (L,P)

# Below are few input matrices
#A = np.array([[4,12,-16],[12,37,-43],[-16,-43,98]])
#A = np.array([[2,-1,0],[-1,2,-1],[0,-1,2]])
#A = np.array([[2,-1,1,-2],[-1,2,-1,1],[1,-1,2,1],[-2,1,1,-1]])
#A = np.array([[2,-1,0,-2,5],[-1,2,-1,1,-3],[0,-1,2,1,4],[-2,1,1,0,1],[-1,3,2,1,-5]])
#A = np.eye(11)
#A = np.random.random([7,7])
A = np.random.random([15,15])


(LA,PA) = mCh(A)

f = open("Cholesky_factorization_output.txt","a+")

f.write("A is:\n")
Am = np.matrix(A)
for line in Am:
    np.savetxt(f,line,fmt='%.2f')

f.write("Modified Cholesky factorization of A is:\n")
LAm = np.matrix(LA)
for line in LAm:
    np.savetxt(f,line,fmt='%.2f')

f.write("A is positive definite: ")
f.write(str(PA))
f.write("\n")
f.close()