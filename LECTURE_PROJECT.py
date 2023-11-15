#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:54:19 2023

@author: n.l.smith
"""


import pandas as pd
import matplotlib.pyplot as mbl
from plotnine import *
import os


os.chdir('/Users/n.l.smith/Desktop/2450 Python')

dat = pd.read_csv("2017_Fuel_Economy_Data.csv")

dat = dat['Combined Mileage (mpg)']

n = len(dat)

# df = pd.DataFrame({"handspan": [20, 20, 19, 24,2, 20, 20.2, 21.5, 
#                                        17, 19.5, 21.5, 18,
#                                        18, 20.5, 20.3, 21.5, 19, 20.4, 
#                                        22.7, 22.9, 17, 23, 
#                                        23.8, 22, 21.5,21.5 ]})


#parameter = 'mean' or 'median' or 'std'


parameter = 'mean'

statList = []

for i in range(1,10_001):

    randSamp = dat.sample(n, replace = True) 
    
    if parameter == 'mean' or 'median' or 'std':
        if parameter == 'std':
            randStanDev = randSamp.std()
            statList.append(float(randStanDev))
            
        if parameter == 'mean':
            randMean = randSamp.mean()
            statList.append(float(randMean))
        
        if parameter == 'median':
            randMedian = randSamp.median()
            statList.append(float(randMedian))
        
    else: 
        raise TypeError("That is not an accepted function")
      

#mbl.hist(xbarList)

#mbl.xlabel("handspan", "kwargs")

#mbl.ylabel("observations")

#mbl.show()


xbarDF = pd.DataFrame({'x': statList})

(
 ggplot(xbarDF, aes( x = 'x')) +
 geom_histogram(size = 3)

)




















