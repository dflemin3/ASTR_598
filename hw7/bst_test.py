# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 15:13:57 2016

@author: dflemin3
"""

import bst
import numpy as np

nums = np.random.randint(low=0,high=999,size=100)

btree = bst.BinarySearchTree()

# Insert 100 random ints into bst
for i in range(0,len(nums)):
    btree.insert(nums[i])
    
# Traverse bst
btree.traverse()