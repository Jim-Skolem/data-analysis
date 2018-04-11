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
data = pd.read_excel('NPAndPDS.xlsx', sheet_name='Sheet1')
d = np.array(data)
#归一化
scaler = preprocessing.MinMaxScaler()
x = scaler.fit_transform(d[:,7:9])
#Kmeans
km = KMeans(n_clusters=2, random_state=10,n_init=10, verbose=0)
#print(km.get_params())
km.fit(x)
clusters=km.labels_
#输出图像
plt.figure(figsize=(8, 8))

i=0
while(i<len(clusters)):
    if clusters[i]==0:
        plt.plot(x[i,0], x[i,1], 'r.', markersize=6)
    else:
        plt.plot(x[i,0], x[i,1], 'g^', markersize=5)
    i=i+1

centers = km.cluster_centers_
    # Draw white circles at cluster centers
plt.scatter(centers[:, 0], centers[:, 1], marker='o',
               c="white", alpha=1, s=400, edgecolor='k')

for i, c in enumerate(centers):
    plt.scatter(c[0], c[1], marker='$%d$' % i, alpha=1,
                    s=100, edgecolor='k')
plt.title('kmeans',fontsize=14, fontweight='bold')
plt.show()

#计算召回率
def count(tag):
    i=0
    x1,y1,x2,y2=0,0,0,0
    while(i<50):
        if clusters[i]==tag:
            x1=x1+1
        else:
            y1=y1+1
        i=i+1
    while(i<100):
        if clusters[i]!=tag:
            x2=x2+1
        else:
            y2=y2+1
        i=i+1
    
    return (x1,y1,x2,y2)

x1,y1,x2,y2=count(tag=1)           

ac=(x1+x2)/100
re=(x1/50+x2/50)/2
pe=(x1/(x1+y2)+x2/(x2+y1))/2

print("\nac=",ac,"\npe=",pe,"\nre=",re)