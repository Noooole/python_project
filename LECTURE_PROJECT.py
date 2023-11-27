# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 14:39:05 2023

@author: brand
"""

from plotnine import *
import pandas as pd
import os

os.chdir("C:/Users/brand/Downloads")



data = pd.DataFrame({"handspan": [17,18,19,20,20,20,22,25]})

class bootstrap(object):
    
    def __init__(self, n = 0, dat = None):
        self._n = n
        self._stat = 'mean'
        self._data = dat
        self._booted = None
        self._cl = 0.95
        
    def set_n(self, n):
        self._n = n
        
    def boot_data_frame(self, type_stat):
        boot_means = []
        
        stat = type_stat.lower()
        self._stat = stat
        
        for i in range(self._n):
            boot_sample = self._data.sample(8, replace = True)
            
            if self._stat == "mean":
                boot_means.append(float(boot_sample.mean()))
            elif self._stat == "median":
                boot_means.append(float(boot_sample.median()))
            elif self._stat == "std":
                boot_means.append(float(boot_sample.std()))
            else:
                raise TypeError("invalid input")
                break
            
        self._booted = pd.DataFrame({"handspan means": boot_means})

#%%

x = bootstrap(1000, data)

x.boot_data_frame("mean")
x.graph()
























