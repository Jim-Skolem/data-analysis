# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 19:32:40 2018

@author: 28414
"""

import pandas as pd
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_samples
from sklearn.cluster import KMeans
from sklearn import preprocessing

data = pd.read_excel('NPAndPDS.xlsx', sheet_name='Sheet1')
d = np.array(data)
#归一化
scaler = preprocessing.MinMaxScaler()
x = scaler.fit_transform(d[:,7:9])
#Kmeans
km = KMeans(n_clusters=2, random_state=10,n_init=10, verbose=0)
km.fit(x)

plt.figure(figsize=(8, 8))
y_km=km.labels_
cluster_labels=np.unique(y_km)
n_clusters =  cluster_labels.shape[0]
silhouette_vals=silhouette_samples(x,y_km,metric='euclidean')
yaxlower,yaxupper=0,0
yticks=[]
for i,c in enumerate(cluster_labels):
    c_silhouette_vals=silhouette_vals[y_km==c]
    c_silhouette_vals.sort()
    yaxupper+=len(c_silhouette_vals)
    color=cm.jet(i/n_clusters)
    plt.barh(range(yaxlower,yaxupper),
             c_silhouette_vals,
             height=1.0,
             edgecolor='none',
             color=color)
    yticks.append((yaxlower+yaxupper)/2)
    yaxlower+=len(c_silhouette_vals)
    
silhouette_avg=np.mean(silhouette_vals)
plt.axvline(silhouette_avg,color="red",linestyle="--")
plt.yticks(yticks,cluster_labels)
plt.show()





   

