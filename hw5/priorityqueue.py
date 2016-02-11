# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 18:01:24 2016

Priority Queue class implimentation

@author: dflemin3
"""

import numpy as np
import math

class PriorityQueue(object):
    # Implimented as a min heap
    def __init__(self, a = None, N = 0, MAX = 100):
        self.a = a # Array to hold data
        self.N = N # Number of elements in priority queue
        self.MAX = MAX # Maximum length
        
        # Init array if it doesn't exist
        if a == None:
            self.a = np.zeros(MAX+1)
            
    # Return minimum value, but don't delete it
    def minimum(self):
        if self.N > 0:
            return self.a[1] # 0th element is ALWAYS empty (otherwise 2*i, 2*i + 1 convention fails)
        else:
            print("Minimum: Empty Priority Queue.")
            return None
    
    # Size of data structure
    def size(self):
        return self.N
    
    # Is it empty?
    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False
    
    # Is it full?
    def isFull(self):
        if self.size() == self.MAX:
            return True
        else:
            return False
          
    # Insert a value assuming tree is a heap tree
    def insert(self,value):
        
        # Do this if it's not full
        if self.isFull():
            print("Insert: Priority Queue is full.")
            return None
        
        # Increase size
        self.N = self.N + 1
        
        # Do the insertion at empty space 1 beyond old N
        self.a[self.N] = value
        
        # Loop until order is achieved
        k = self.N
        
        # Start at bottom, run as long as you're not at root, 
        # and parent > child (opposite order of what we want)
        # Use floor since python 3 removes interger division
        while(k > 1 and self.a[math.floor(k/2)] > self.a[k]):
            # Exchange parent with child
            temp = self.a[math.floor(k/2)]
            self.a[math.floor(k/2)] = self.a[k]
            self.a[k] = temp
            
            # Decrease k to go up 1 level
            k = math.floor(k/2)
            
    # Remove/return the minimum value from the top.
    # Note: It requires fixing the tree since the root
    # is empty.  What we do is put the last one on the top,
    # Then iterate until order is achieved
    def delMin(self):
        
        tmp = 0.0
        j = 0
        
        if self.isEmpty():
            print("Error: Empty Priority Queue.")
        
        # Value to return later
        minimum = self.a[1]
        
        # Put last value at top
        self.a[1] = self.a[self.N]
        self.a[self.N] = 0        
        self.N = self.N - 1 # Move the end back
        
        # Swap with smallest child, repeat until properly ordered
        k = 1 # Start loop at root, descend tree
        while (2*k <= self.N): # <= since 2 children
            # Note: Right child is 2k + 1, left child is 2k
            # Also, if relies on short-circuit behavior
            if((2*k == self.N) or self.a[2*k] < self.a[2*k +1]): # child is last one, or left less than right
                j = 2*k # Lesser child or only child
            else:
                j = 2*k + 1 # Right child exists and is less than left child
          
            # See if heap has been ordered by checking if
            # parent < child
            if(self.a[k] > self.a[j]):
                tmp = self.a[k]
                self.a[k] = self.a[j]
                self.a[j] = tmp
                k = j
            else:
                # Binary heap condition satisfied
                # aka parent < child
                break
        
        return minimum