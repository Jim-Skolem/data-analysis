# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 11:07:36 2017

@author: 28414
"""

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic

data1 = pd.read_excel('totalNPdata.xlsx', sheet_name='Sheet1')
data2 = pd.read_excel('totalPDSdat.xlsx', sheet_name='Sheet1')
n1=data1[0:1]

d= {'age':n1['b'], 'weight': n1['c'], 'hight': n1['d']}
mosaic(d)
plt.show()
