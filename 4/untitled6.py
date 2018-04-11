# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 10:12:30 2017

@author: 28414
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA   

data1 = pd.read_excel('totalNPdata.xlsx', sheet_name='Sheet1')
data2 = pd.read_excel('totalPDSdat.xlsx', sheet_name='Sheet1')

a=data2[['e','m']]
X,Y=data2['e'],data2['m']

ax1=plt.subplot(111)
ax1.set_ylabel('youbuchang')
ax1.set_xlabel('zuobuchang')
plt.scatter(X,Y, marker = '.')
plt.show()

ax2=plt.subplot(111)
pca=PCA(n_components=1)
pcaData=pca.fit_transform(a)
ax2=sns.stripplot(pcaData,jitter=False)
plt.show()