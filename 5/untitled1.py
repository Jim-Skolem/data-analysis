# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 10:33:20 2017

@author: 28414
"""

import pandas as pd
from sklearn.neighbors import NearestNeighbors 

data = pd.read_excel('totalNPdata1.xlsx', sheet_name='Sheet1')
losedata = pd.read_excel('losedata.xlsx', sheet_name='Sheet1')
lsda= pd.read_excel('losedata0.xlsx', sheet_name='Sheet1')
k=20
nbrs = NearestNeighbors(n_neighbors=k, algorithm="kd_tree").fit(data) 
distances, indices = nbrs.kneighbors(losedata)

i=0
while(i<9):
    j=0
    sum=0
    dsum=0
    while(j<k):
        dsum=dsum+1/distances[i,j]
        j=j+1
    j=0
    while(j<k):
        sum=sum+(1/distances[i,j])*(data.loc[indices[i,j],'b'])/dsum
        j=j+1
    losedata.loc[i,'b']=sum
    i=i+1

i=0
psum=0
for a in losedata['b']:
    p=0
    p=(lsda.loc[i,'b']-losedata.loc[i,'b'])**2/(lsda.loc[i,'b'])**2
    psum=psum+p
    i=i+1
    
p=1-psum/i
print("p=",p)