# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 00:38:38 2016

Stack implimentation

@author: dflemin3
"""

# to be python 3 compatitible
from __future__ import print_function, division

class Node(object):
    def __init__(self, data = None, nxt = None):
        self.data = data # Node's data
        self.nxt = nxt # Node this Node points to
        
class Stack(object):
    def __init__(self, head = None, N = 0):
        self.head = head # Head node [Node]
        self.N = N # size of Stack [int]  
    
    def isEmpty(self):
        if self.N == 0:
            return True
        else:
            return False
        
    def size(self):
        return self.N
        
    # Like insert at head for linked list
    def push(self,value = None):
        new_top = Node(data=value,nxt=None)
        new_top.nxt = self.head
        self.head = new_top
        
        # Increase size of stack
        self.N = self.N + 1
        
    # Remove, return value at head
    def pop(self):
        # Make sure Stack isn't empty
        if self.head == None or self.N == 0:
            print("Pop: Empty stack.")
            return None
        else:
            ret = self.head.data

            # Get rid of old head, trust python for memory management
            self.head = self.head.nxt

            # Decrease size
            self.N = self.N - 1

            # Return old head's contents
            return ret
        
    # Same as pop, but don't remove the head
    def top(self):
        if self.head == None or self.N == 0:
            print("Top: Empty stack.")
            return None
        else:
            return self.head.data
        
    # Print out the stack
    def __repr__(self):
        # Case: empty stack
        if self.head == None or self.N == 0:
            return "Empty stack."
        
        word = 'top '
        n = self.head
        while(n.nxt != None):
            word += (str(n.data) + ' ')
            n = n.nxt
            
            # Next one is end: special case
            if n.nxt == None:
                word += (str(n.data) + ' ') 
                break
                
        return word + 'bottom'