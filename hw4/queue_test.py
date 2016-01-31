# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 20:29:57 2016

Scipt to test the Queue class

@author: dflemin3
"""
from __future__ import print_function
import queue

tmp = queue.Queue()

print("Putting 0-9 on the Queue.\n")
for i in range(0,10):
    print("Put:",i)
    tmp.put(i)
    
print("\n")
print("Getting values from Queue.\n")
while(tmp.front() != None):
    got = tmp.get()
    print("Get:",got)