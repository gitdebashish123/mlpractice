#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 22:22:18 2018
# Subject : Tupples
@author: debashish.kheti
"""

# Tuples are list only but you can't perform any operation of remove/add
# A sequence of immutable python objects
# List [] ,Tuples ()
# To make any change to tuple you need to define one more tuple
# if we have list why are we using tuples ? since tuples are immutable, iterating
# through tuples are faster, it guarantees that data is write protected
# for constant set of elements , go for tuples


subjects = ('physics','chemistry','maths')
games = ('football','crcket','tennis')

# append - doesn't work

# Index

print(subjects[1])

#Index of 

print(subjects.index('maths'))

#Slicing

print(subjects[0:2])

# Concat

data = subjects + games
print(data)

# We can define Tuples inside a list

Combine = [('physics','chemistry','maths'),('football','crcket','tennis')]

# to print cricket

print(Combine[1][1])

Combine = [('physics','chemistry','maths'),('football','crcket')]

print(Combine[1][1])
