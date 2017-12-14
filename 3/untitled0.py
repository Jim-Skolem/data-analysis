# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 22:37:23 2017

@author: 28414
"""

import pandas as pd
import seaborn as sns;
import matplotlib.pyplot as plt

data1 = pd.read_excel('totalNPdata.xlsx', sheet_name='Sheet1')
data2 = pd.read_excel('totalPDSdat.xlsx', sheet_name='Sheet1')

x=data2['e']
y=data2['m']

plt.figure(figsize=(8,8))
ax = sns.kdeplot(x, y, shade=True)
ax1 = sns.kdeplot(x, y, cbar=True)