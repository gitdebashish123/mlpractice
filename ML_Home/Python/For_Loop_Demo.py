#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 23:35:27 2018
Subject : Pyhton For/While Loop
@author: debashish.kheti
"""
alphabets = ['a','b','c','d','e']

for x in alphabets:
    print(x)
    
# Break/Continue

for x in alphabets:
    if x == 'c':
        print('alphabets found')
        break
    else:
        print('not found')
        
for x in alphabets:
    if x == 'c':
        print('alphabets found')
        continue
    else:
        print('not found')
        
for i in range(10):
    print(i)
        
# output : print 0 to 9

for i in range(2,10):
    print(i)
# output : print 2 to 9

############While Loop################
    
i=0

while i < 10:
    print(i)
    i += 1