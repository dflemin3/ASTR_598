# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 00:50:06 2016

Testing stack.py

@author: dflemin3
"""

from __future__ import print_function

import stack 

test = stack.Stack()

print("Pushing to stack:")
for i in range(0,10):
    print(i)
    test.push(i)
    
print("stack:",test)
print("size:",test.N)

print("Popping from stack.")
s_n = test.N
for i in range(0,s_n):
    print(test.pop())
    
print("stack:",test)
print("Is the stack empty?",test.isEmpty())