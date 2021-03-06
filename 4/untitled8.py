# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 10:29:38 2017

@author: 28414
"""

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import manifold

data1 = pd.read_excel('totalNPdata.xlsx', sheet_name='Sheet1')
data2 = pd.read_excel('totalPDSdat.xlsx', sheet_name='Sheet1')

a=data1[['b','c','d']]
X,Y,Z=data1['b'],data1['c'],data1['d']

fig = plt.figure()
ax = Axes3D(fig)
plt.scatter(X,Y,Z, marker = '.')
ax.set_title("age-weight-hight")
ax.set_zlabel('hight') 
ax.set_ylabel('weight')
ax.set_xlabel('age')
plt.show()

ax1=plt.subplot(111)
clf = manifold.MDS(n_components=2, n_init=1, max_iter=100)
X_mds = clf.fit_transform(a)
x=X_mds[:, 0:1]
y=X_mds[:, 1:2]
plt.scatter(x,y, marker = '.')
ax1.set_title("MDS")
ax1.set_ylabel('Y')
ax1.set_xlabel('X')
plt.show()

'''

'''