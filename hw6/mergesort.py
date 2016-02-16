# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 10:08:32 2016

@author: dflemin3
"""

import numpy as np

# Divide step
def sort(a, low, high, aux):
    # Base case
    if(high <= low):
        return
    
    # Find the midpoint, then recursively sort
    mid = low + int((high - low)/2)
    sort(a, low, mid, aux) # Sort left half
    sort(a, mid+1, high, aux) # Sort right half
    
    # Merge sorted low, high arrays
    merge(a, low, mid, high, aux)

def merge(a, low, mid, high, aux):
    i = low
    j = mid+1
    k = i
    
    # Make a copy
    #for k in range(low,high+1):
    aux[low:high+1] = a[low:high+1]
    
    k = low
    while(k <= high):
        while((i <= mid) and (j <= high)):
            if(aux[j] < aux[i]):
                a[k] = aux[j]
                j += 1
                k += 1
            else:
                a[k] = aux[i]
                i += 1
                k += 1
                
        # Whichever is smaller array, copy it
        while(i <= mid):
            a[k] = aux[i]
            i += 1
            k += 1
        while(j <= high):
            a[k] = aux[j]
            j += 1
            k += 1
            
# Given an array a, sort it
def mergesort(a):
    aux = np.copy(a)
    sort(a,0,len(a)-1,aux)
    return a