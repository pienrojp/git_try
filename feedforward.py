#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 23:19:24 2017

@author: panin
"""

import numpy as np
import matplotlib.pyplot as plt

Nclass = 500

X1= np.random.randn(Nclass,2)+np.array([0,-2])
X2= np.random.randn(Nclass,2)+np.array([2,2])
X3= np.random.randn(Nclass,2)+np.array([-2,2])
X = np.vstack([X1,X2,X3])

Y=np.array([0]*Nclass +[1]*Nclass+[2]*Nclass)

plt.scatter(X[:,0], X[:,1], c=Y, s=100, alpha=0.5)
plt.show()

D=2
M =3
K=3

def forward(X,w1,b1,w2,b2):
    Z = 1/(1+np.exp(-X.dot(w1)-b1))
    A = Z.dot(w2)
    expA = np.exp(A)
    Y = expA/expA.sum(axis=1, keepdims=True)
    return Y
    
def classification_rate(Y,P):
    correct = 0
    total = 0
    for i in range(len(Y)):
        total += 1
        if Y[i]==P[i]:
            correct += 1
    return correct/total
    
w1 = np.random.rand(D, M)
b1 = np.random.rand(M)
w2 = np.random.rand(M, K)
b2 = np.random.rand(K)

    
P_Y_given = forward(X,w1,b1,w2,b2)
P = np.argmax(P_Y_given,axis=1)

print(classification_rate(Y,P))
