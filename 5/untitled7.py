# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 23:16:38 2017

@author: 28414
"""

import pandas as pd
from sklearn.neighbors import NearestNeighbors 

data = pd.read_excel('totalNPdata1.xlsx', sheet_name='Sheet1')
losedata = pd.read_excel('losedata.xlsx', sheet_name='Sheet1')
lsda= pd.read_excel('losedata0.xlsx', sheet_name='Sheet1')
k=18
nbrs = NearestNeighbors(n_neighbors=k, algorithm="kd_tree").fit(data) 
distances, indices = nbrs.kneighbors(losedata)

i=0
for a in indices:
    sum=0
    for x in a:
        sum=sum+data.loc[x,'b']              
    losedata.loc[i,'b']=sum/k
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

