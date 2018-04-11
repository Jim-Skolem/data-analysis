#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 10:30:16 2018

@author: jim
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Kmodes.kmodes.kmodes import KModes

data1 = pd.read_excel('totalNPdata.xlsx', sheet_name='Sheet1')
data2 = pd.read_excel('totalPDSdat.xlsx', sheet_name='Sheet1')

x=data1[['c','d']]
km = KModes(n_clusters=2, verbose=1)
clusters = km.fit_predict(x)
plt.figure(figsize=(5, 5))
color = ("red", "green")
colors=np.array(color)[clusters]
plt.scatter(x['c'],x['d'],c=colors,marker=".")
plt.show()