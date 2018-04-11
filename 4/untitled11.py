# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 11:11:08 2017

@author: 28414
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import manifold

data1 = pd.read_excel('totalNPdata.xlsx', sheet_name='Sheet1')
data2 = pd.read_excel('totalPDSdat.xlsx', sheet_name='Sheet1')
n_neighbors = 30

a=data2[['b','c','d']]

ax1=plt.subplot(111)
iso = manifold.Isomap(n_neighbors, n_components=2).fit_transform(a)
x=iso[:, 0:1]
y=iso[:, 1:2]
plt.scatter(x,y, marker = '.')
ax1.set_title("ISOMAP")
ax1.set_ylabel('Y')
ax1.set_xlabel('X')
plt.show()