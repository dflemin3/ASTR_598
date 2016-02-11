# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 18:05:18 2016

Test the priority queue

@author: dflemin3
"""

from __future__ import print_function

import numpy as np
import priorityqueue as priq

pq = priq.PriorityQueue()

print("Add 20 random ints to the priority queue.\n")
rand_ints = np.random.randint(0,100,size=20)

for i in range(0,len(rand_ints)):
    print("Inserting into pq:",rand_ints[i])    
    pq.insert(rand_ints[i])
    
print("\nCall delMin() 20 times.\n")
for i in range(0,len(rand_ints)):
    print("delMin():",pq.delMin())    