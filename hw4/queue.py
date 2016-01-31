# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 20:26:00 2016

Queue class implimentation

@author: dflemin3
"""

class Node(object):
    def __init__(self, data = None, nxt = None):
        self.data = data # Node's data
        self.nxt = nxt # Node this Node points to

class Queue(object):
    def __init__(self, head = None, tail = None, N = 0):
        self.head = head
        self.tail = tail
        self.N = N
     
    def isEmpty(self):
        if self.N == 0:
            return True
        else:
            return False
        
    def size(self):
        return self.N
    
    def put(self,value):
        n = Node(data = value, nxt = None)
        
        # Case: empty Queue
        if(self.head == None):
            self.head = n
            self.tail = n
        # Case: 1 node
        elif(self.head == self.tail):
            self.head.nxt = n
            self.tail = n
        # Case: general
        else:
            self.tail.nxt = n
            self.tail = n
            
        # Increment size
        self.N = self.N + 1
    
    def get(self):
        # Case: Empty Queue
        if(self.head == None):
            print("Get error: Empty Queue.")
            return None
        else:
            ret = self.head.data

            # Set head to nxt, decrease size, return 
            self.head = self.head.nxt
            self.N = self.N - 1
            return ret
        
    # Like get, but does not remove head
    def front(self):
        # Case: Empty Queue
        if(self.head == None):
            return None
        else:
            ret = self.head.data
            return ret