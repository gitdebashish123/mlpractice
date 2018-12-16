#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 01:00:00 2018

@author: debashish.kheti
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/debashish.kheti/Desktop/ML_Home/input_files/headbrain.csv')

data.head(5)
print(data.shape)

#Collection head and size

x=data['Head Size(cm^3)'].values
y=data['Brain Weight(grams)'].values

print(x)

mean_x=np.mean(x)
mean_y=np.mean(y)

#number of values

m=len(x)

#calculate the values of m & c

numer=0
denom=0

for i in range(m):
    numer+=(x[i]-mean_x)*(y[i]-mean_y)
    denom+=(x[i]-mean_x)**2
b1=numer/denom
b0=mean_y-(b1*mean_x)

print(b1,b0)

min_x=np.min(x)-100
max_x=np.max(x)+100

X=np.linspace(min_x,max_x,1000)
print(X.shape)
Y=b0+b1*X
print(Y.shape)

plt.plot(X,Y,label='Regression Line')
plt.scatter(x,y,label='Scatter Plot')
plt.xlabel('Head Size(cm^3)')
plt.ylabel('Brain Weight(grams)')
plt.legend()
plt.show


##Additional

X=pd.DataFrame({3000})
print(X.shape)
Y=b0+b1*X
print(Y.shape)

plt.plot(X,Y,label='Regression Line')
plt.scatter(x,y,label='Scatter Plot')
plt.xlabel('Head Size(cm^3)')
plt.ylabel('Brain Weight(grams)')
plt.legend()
plt.show


##########Alternative Method##################


