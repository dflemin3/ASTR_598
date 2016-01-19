"""
David Fleming Jan. 2016

Hw2: Linked List implimentation for
Astr 598
"""

from __future__ import print_function

# Node class for part (a)
class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node
        
    def __repr__(self):
        # How to represent the class
        return str(self.data)

# Linked List class for part (b)        
class LinkedList(object):
    def __init__(self, head = Node(), tail = Node(), size = 0):
        self.head = head
        self.tail = tail
        self.size = size
        
        # Ensure init proper behavior
        if self.head.data != None and self.tail.data != None:
            self.size = 2
            head.next_node = self.tail
            tail.next_node = None
        # No tail
        elif self.head.data != None and self.tail.data == None:
            self.size = 1
            self.head.next_node = None
            self.tail = self.head
        # No head
        elif self.head.data == None and self.tail.data != None:
            self.size = 1
            self.tail.next_node = None
            self.head = self.tail
        else:
            self.tail = None
            self.head = self.tail
            self.size = 0
    
    # Class methods for inserting new nodes
    def insert_at_tail(self,value):
        # Case: Empty linked list
        if (self.size == 0):
            self.tail = Node(value,None)
            self.head = self.tail 
        
        # Case: one node
        elif(self.size == 1):
            new_tail = Node(value,None)
            self.head.next_node = new_tail
            self.tail = new_tail
            
        # General case:
        else:
            new_tail = Node(value, None)
            self.tail.next_node = new_tail
            self.tail = new_tail
        
        self.size = self.size + 1
    
    
    def insert_at_head(self,value):
        # Case: list is empty
        if (self.size == 0):
            self.head = Node(value,None)
            self.tail = self.head
        
        # Case: one node
        elif (self.size == 1):
            old_head = self.head
            new_head = Node(value,None)
            new_head.next_node = old_head
            self.head = new_head
        
        # General case: list has stuff
        else:
            new_head = Node(value, None)
            old_head = self.head
            new_head.next_node = old_head
            self.head = new_head
    
        self.size = self.size + 1
    
    # Delete head and return value
    def delete_at_head(self):
        # Case: list is empty, no head
        if self.head == None:
            return None
        
        # General case: list has stuff
        else:
            old_head = self.head.data
            self.head = self.head.next_node
            self.size = self.size - 1
            return old_head
    

    # Delete tail and return value
    # Slow: O(~n)
    def delete_at_tail(self):
        n = self.head
        
        # Case: Empty list
        if n == None:
            return None
        
        # Case: 1 object (at tail already)
        if n.next_node == None:
            ret = n.data
            self.head = None
            self.tail = self.head
            self.size = self.size - 1
            return ret
        
        while(n != None):
            # If at node before tail
            if n.next_node == self.tail:
                ret = n.next_node.data
                n.next_node = None
                self.tail = n
                self.size = self.size - 1
                return ret
            n = n.next_node
            
    def print_self(self):
        n = self.head
        print("Head")

        while(n != None):
            print(n.data)
            
            # See if next is tail
            if(n.next_node == None):
                #print(n.data)
                print("Tail")
                break
            n = n.next_node
        print("Size:",self.size,"\n")
        
# Run code for part (d)
ll = LinkedList()

# Print empty list
ll.print_self()

#Add 3 elements at the head
print("Inserting 0  at head.")
ll.insert_at_head(0.0)
ll.print_self()

print("Inserting 2 at head.")
ll.insert_at_head(2.0)
ll.print_self()

print("Inserting -5 at head.")
ll.insert_at_head(-5)
ll.print_self()

print("Deleting at head:",ll.delete_at_head())
ll.print_self()

print("Inserting 3 at tail.")
ll.insert_at_tail(3)
ll.print_self()

print("Inserting 4 at tail.")
ll.insert_at_tail(4)
ll.print_self()

print("Inserting 19 at tail.")
ll.insert_at_tail(19)
ll.print_self()