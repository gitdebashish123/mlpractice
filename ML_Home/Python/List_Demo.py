#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 21:43:09 2018
Subject : List
@author: debashish.kheti
"""
# List
fruits = ['abc','pqr','xyz']
print(fruits)

subjects = ['physics','chemistry','maths']

games = ['football','crcket','tennis']

#Append - appends an object to the list
subjects.append('history')
print(subjects)

x = [1,2,3]
x.append(5)
print(x)

#Inserts - have to specify index value

subjects.insert(1,'history')
print(subjects)

#Extends - appends elements of an object

subjects.extend(games)
print(subjects)

#Remove

subjects.remove('chemistry')
print(subjects)

#Reverse

subjects.reverse()
print(subjects)

#Concat-No conact available, have to use +

print(subjects+games)


# Comparing extend vs in_place add operater
# Theory says + is better but extend performance is better than + operator
import time
x = range(100000)
y = range(100000)

t1 = time.clock()
x.extend(y)
t2 = time.clock() - t1

t3 = time.clock()
x + y
t4 = time.clock() - t3

print("t2 extend : "+t2)
print("t4 in_place : "+t4)


# Membership Testing

x = ['abc','pqr','xyz']

if 'abd' in x:
    print("it's a member")
else:
    print("not a member")
