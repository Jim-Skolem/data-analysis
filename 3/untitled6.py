# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 23:26:02 2017

@author: 28414
"""

import pandas as pd
import numpy as np
import seaborn as sns; sns.set(style="ticks", color_codes=True)
import matplotlib.pyplot as plt

data1 = pd.read_excel('totalNPdata.xlsx', sheet_name='Sheet1')
data2 = pd.read_excel('totalPDSdat.xlsx', sheet_name='Sheet1')

a=data1[['b','c','d','e']]
b=data2[['b','c','d','e']]

plt.figure(figsize=(7,7))
g1 = sns.pairplot(a)
plt.figure(figsize=(7,7))
g2 = sns.pairplot(b)


