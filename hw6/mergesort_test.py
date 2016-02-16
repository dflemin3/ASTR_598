# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 12:35:38 2016

@author: dflemin3
"""

from __future__ import print_function
from functools import partial

import numpy as np
import mergesort
import timeit

n = [100,10000,1000000,100000000]

for i in range(0,len(n)):

    arr = np.random.randint(low=0,high=n[i],size=n[i])

    ans = np.mean(timeit.Timer(partial(mergesort.mergesort,arr)).repeat(repeat=1,
                  number=1))
    print(n[i],ans,'seconds')
