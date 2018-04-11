# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 21:18:53 2017

@author: 28414
"""
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA   

data1 = pd.read_excel('totalNPdata.xlsx', sheet_name='Sheet1')
data2 = pd.read_excel('totalPDSdat.xlsx', sheet_name='Sheet1')

a=data1[['b','c','d']]
X,Y,Z=data1['b'],data1['c'],data1['d']

fig = plt.figure()
ax = Axes3D(fig)
plt.scatter(data1['b'],data1['c'],data1['d'], marker = '.')
ax.set_zlabel('hight') 
ax.set_ylabel('weight')
ax.set_xlabel('age')
plt.show()

pca=PCA(n_components=2)
pcaData=pca.fit_transform(a)
ax1=plt.subplot(111)
x=pcaData[:, 0:1]
y=pcaData[:, 1:2]
ax1.set_title("PCA")
ax1.set_ylabel('Y')
ax1.set_xlabel('X')
plt.scatter(x,y, marker = '.')
plt.show()