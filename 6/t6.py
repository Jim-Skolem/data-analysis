# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 10:17:54 2018

@author: 28414
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from Kmodes.kmodes.kmodes import KModes

data1 = pd.read_excel('totalNPdata.xlsx', sheet_name='Sheet1')
data2 = pd.read_excel('totalPDSdat.xlsx', sheet_name='Sheet1')
data3 = pd.read_excel('NPAndPDS.xlsx', sheet_name='Sheet1')
d3 = np.array(data3)
x = d3[:,0:4]
'''
#因为使用的是汉明距离，所以应该不用归一化
scaler = preprocessing.MinMaxScaler()
x = scaler.fit_transform(d3)
'''
km = KModes(n_clusters=2,init='Huang',n_init=5, verbose=1)
clusters = km.fit_predict(x)
