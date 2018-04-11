# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 18:48:02 2018

@author: 28414
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import preprocessing

data1 = pd.read_excel('totalNPdata.xlsx', sheet_name='Sheet1')
data2 = pd.read_excel('totalPDSdat.xlsx', sheet_name='Sheet1')
data3 = pd.read_excel('NPAndPDS.xlsx', sheet_name='Sheet1')

a = np.array(data3)
min_max_scaler = preprocessing.MinMaxScaler()
X_train_minmax = min_max_scaler.fit_transform(a[:,4:])

km = KMeans(n_clusters=2,random_state=100).fit_predict(X_train_minmax)
