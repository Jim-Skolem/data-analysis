# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 10:17:54 2018

@author: 28414
"""

import numpy as np
import pandas as pd
from matplotlib import cm
import matplotlib.pyplot as plt
from sklearn import preprocessing
from Kmodes.kmodes.kmodes import KModes
from sklearn.metrics import silhouette_samples
from Kmodes.kmodes.util.dissim import matching_dissim, ng_dissim

data = pd.read_excel('NPAndPDS.xlsx', sheet_name='Sheet1')
d3 = np.array(data)
x = d3[:,0:4]
'''
#因为使用的是汉明距离，所以应该不用归一化
scaler = preprocessing.MinMaxScaler()
x = scaler.fit_transform(d3)
'''
'''
cat_dissim : func, default: matching_dissim
'''
km = KModes(n_clusters=2,
            cat_dissim=ng_dissim,
            init='Huang',
            n_init=10,
            verbose=0)
km.fit(x)
clusters = km.labels_
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

x1,y1,x2,y2=count(tag=0)           

ac=(x1+x2)/100
re=(x1/50+x2/50)/2
pe=(x1/(x1+y2)+x2/(x2+y1))/2

print("\nac=",ac,"\npe=",pe,"\nre=",re)
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



