#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 19:24:37 2021

@author: jackryan
"""

###import libraries
###import libraries
 
import pandas as pd
 
#import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
###import csv and define array
 
blended_Data = pd.read_csv(r"/Users/jackryan/Downloads/BlendedData.csv")
###currency function: truncate values to have M or B
 
'''def currency(blended_Data): 
    """The two args are the value and tick position"""
    x = blended_Data['value']
    x_mean = np.mean(x)
    if x_mean >= 1000000:
        s = '${:1.1f}M'
    else:
        s = '${:1.0f}K'
 
    return s'''
###charting function
 
def Charts(blended_Data):
    Fig, axes = plt.subplots(nrows = 1, ncols = 1, figsize = (9,4))
    blended_Data['value'] = blended_Data['value'] / 1000000000
    blended_Data.set_index('date', inplace = True)
    blended_Data.groupby('source')['value'].plot(legend=True)
    Fig1 = sns.lineplot()
    Fig1.set(xlabel = 'Years', ylabel = 'Balance')
    fmt = '${x:,.0f}B'
    tick = mtick.StrMethodFormatter(fmt)
    axes.yaxis.set_major_formatter(tick) 
    plt.xticks(rotation=25)
    plt.xlabel("Year")
    plt.ylabel("Value")
    plt.title("Blended C&I Forecast, All Values are in Billions")
    plt.show()
Charts(blended_Data)
