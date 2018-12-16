#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 23:03:02 2018
Subject : Set
@author: debashish.kheti
"""

# Set
subjects = {'physics','chemistry','maths','maths'}
print(subjects)

#Output : {'chemistry', 'maths', 'physics'}

#Tuple
subjects = ('physics','chemistry','maths','maths')
print(subjects)
#Output : ('physics', 'chemistry', 'maths', 'maths')


#List
subjects = ['physics','chemistry','maths','maths']
print(subjects)
#Output : ['physics', 'chemistry', 'maths', 'maths']


# Set is a sequence that contains unique objects
# all elements are immutable


a = {1,2,3,4,5,6}
b = {5,6,7,8,9}

# Union

print(a | b)
# {1, 2, 3, 4, 5, 6, 7, 8, 9}
# Intersection

print(a & b)
# {5, 6}

# Minus

print( a - b)
#{1, 2, 3, 4}

# symetric difference.
print( a ^ b)
#{1, 2, 3, 4, 7, 8, 9}

# Type conversion can be possible between List,Tuple and Set