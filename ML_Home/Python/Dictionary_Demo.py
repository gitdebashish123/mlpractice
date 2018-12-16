#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 00:06:07 2018
Subject : Pyhthon Data Dictionary
@author: debashish.kheti
"""

student = {'name':'debahish','age':30,'courses':['maths','physics']}

print(student['name'])
print(student['courses'])
print(student['dob']) #KeyError: 'dob'

print(student.get('courses'))
print(student.get('dob'))
print(student.get('dob','not found')) #similar to coalesce

# Adding New Entries to Dictionary

student['dob']='03-10-1989'
print(student)


# update a value

student['age']=29
print(student)

#Update multiple values : Takes List as an argument

student.update({'age':28,'courses':['chemistry','physics']})
print(student)

# Print all keys or all values

print(student.keys())
print(student.values())
print(student.items()) # Returns pairs of key-value

#Checking key exists or not
if 'debashish' in student:
    print('Exists')
else:
    print('dosen\'t exists')
    
#OP: dosen't exists
    
if 'name' in student:
    print('Exists')
else:
    print('dosen\'t exists')
#OP: Exists
    
#Deleting Key elements
    
del student['name']
print(student)
# Note POP also returns the delete values
student.pop('dob')

dob = student.pop('dob')
print(dob)



# If we loop throug the key without using any method it'll just return all the keys

for key in student:
    print(key)

# loop through keys and values
    
for k,v in student.items():
    print(k,v)