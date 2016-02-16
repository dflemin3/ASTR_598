# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 13:04:45 2016

@author: dflemin3
"""

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8,8))

numbers = np.asarray([1.0e2,1.0e4,1.0e6,1.0e8])
time = np.asarray([0.00125098228455,0.106668949127,15.0660820007,1941.47644281])
               
const = 2.5e-6
theory = const*numbers*np.log10(numbers)

ax.plot(numbers,time,lw=3,label=r'Computed Time')
ax.plot(numbers,theory,lw=3,label=r'%.2e * NlogN' % const)

ax.set_xlabel('Number of Ints')
ax.set_ylabel('Time [seconds]')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_title('Mergesort Scaling')
ax.legend(loc='upper left')
ax.grid(True)
fig.savefig("mergesort_scaling_DavidFleming.png")
