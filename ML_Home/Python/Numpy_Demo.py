#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 14:31:42 2018

@author: debashish.kheti
"""

import numpy as np
a=np.array([(1,2,3),(4,5,6)])
print(a)

##Calculating List Size

import numpy as np
import sys
import time

S = range(1000)
print(sys.getsizeof(5)*len(S))

D = np.arange(1000)

print(D.size*D.itemsize)

#######

SIZE = 1000000

L1 = range(SIZE)
L2 = range(SIZE)

A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start=time.time()

result = [(x,y) for x,y in zip(L1,L2)]

print((time.time()-start)*1000)

start=time.time()

result = A1 + A2 

print((time.time()-start)*1000)

#List Vs NumPy
# Numpy occupy  less memory than List
# Numpy is faster than List

###### More operations

a = np.array([(1,2,3),(2,3,4),(4,5,6)])
print(a)
print(a.ndim)
print(a.dtype)
print(a.size)
print(a.itemsize)
print(a.nbytes)
print(a.size*a.itemsize)
print(a.shape)

#nbytes= x.itemsize * x.size
#size-total elements,itemsize-- individual element size
# shape=row X column

#shape/reshape Array
a = np.array([(1,2,3),(2,3,4),(4,5,6),(4,5,6)])
a.shape
a.reshape(3,4)

#Slicing Array
a = np.array([(1,2,3),(2,3,4),(4,5,6),(4,5,8)])
print(a[0,2])
#all rows 2nd elememt
print(a[0:,2])
print(a[0:3,2])

a = np.linspace(1,3,5)
print(a)


## axis-1 - ROWS , axis-0 - COLUMNS

a = np.array([(1,2,3),(2,3,4),(4,5,6),(4,5,8)])
print(a.sum(axis=0))
print(a.sum(axis=1))

a = np.array([(1,2,3),(2,3,4),(4,5,6),(4,5,8)])
print(np.sqrt(a))
print(np.std(a))


a = np.array([(1,2,3),(2,3,4),(4,5,6),(4,5,8)])
b = np.array([(1,2,3),(2,3,4),(4,5,6),(4,5,8)])

print(a+b)
print(np.vstack((a,b)))
print(np.hstack((a,b)))
print(np.ravel(a))