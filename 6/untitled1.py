# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 19:06:23 2018

@author: 28414
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import preprocessing
#数据
data = pd.read_excel('NPAndPDS.xlsx', sheet_name='Sheet1')
d = np.array(data)
#归一化
scaler = preprocessing.MinMaxScaler()
x = scaler.fit_transform(d[:,7:9])
#Kmeans
distortions=[]
for i in range(1,11):
    km=KMeans(n_clusters=i,
              init='k-means++',
              n_init=10,
              max_iter=300,
              random_state=0)
    km.fit(x)
    distortions.append(km.inertia_)
plt.figure(figsize=(8, 8))
plt.plot(range(1,11),distortions,marker='o')
plt.xlabel('number of cluster')
plt.ylabel('distortion')
plt.title("Elbow Method",fontsize=14, fontweight='bold')
plt.show()