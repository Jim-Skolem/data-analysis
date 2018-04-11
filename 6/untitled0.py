#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 22:14:02 2018

@author: jim
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import preprocessing
#数据
data1 = pd.read_excel('totalNPdata.xlsx', sheet_name='Sheet1')
data2 = pd.read_excel('totalPDSdat.xlsx', sheet_name='Sheet1')
d = np.array(data1)
d=np.delete(d,29,0)
d=np.delete(d,170,0)
#归一化
scaler = preprocessing.MinMaxScaler()
x = scaler.fit_transform(d[:,10:12])
#Kmeans
kmeans = KMeans(n_clusters=2, random_state=10)
print(kmeans.get_params())
kmeans.fit(x)
km=kmeans.labels_
#输出图像
plt.figure(figsize=(7, 7))
'''
color = ("red", "green")
colors=np.array(color)[km]
#plt.scatter(data1['j'],data1['k'],c=colors,marker=".")
'''
'''
i=0
while(i<len(km)):
    if km[i]==0:
        plt.plot(d[i,10], d[i,11], 'r.', markersize=6)
    else:
        plt.plot(d[i,10], d[i,11], 'g^', markersize=5)
    i=i+1
plt.title('kmeans')
#plt.plot(data1['k'], data1['l'], 'k.', markersize=4)
plt.figure(figsize=(7, 7))
'''
i=0
while(i<len(km)):
    if km[i]==0:
        plt.plot(x[i,0], x[i,1], 'r.', markersize=6)
    else:
        plt.plot(x[i,0], x[i,1], 'g^', markersize=5)
    i=i+1

centers = kmeans.cluster_centers_
    # Draw white circles at cluster centers
plt.scatter(centers[:, 0], centers[:, 1], marker='o',
               c="white", alpha=1, s=400, edgecolor='k')

for i, c in enumerate(centers):
    plt.scatter(c[0], c[1], marker='$%d$' % i, alpha=1,
                    s=100, edgecolor='k')
plt.title('kmeans')
plt.show()


'''
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1],
            marker='x',s=169, linewidths=3,
            color='k', zorder=10)
-------------------------------------------------------
x=data3[['c','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x']]

plt.figure(figsize=(8, 8))
color = ("red", "green")
colors=np.array(color)[kl]
marker=('.','x')
markers=np.array(marker)[kl]
plt.scatter(x['j'],x['k'],c=colors)
plt.show()
'''