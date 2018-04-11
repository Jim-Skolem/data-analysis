# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 21:46:03 2017

@author: 28414
"""
import pandas as pd
from sklearn.preprocessing import Imputer

data = pd.read_excel('totalNPdata1.xlsx', sheet_name='Sheet1')
losedata = pd.read_excel('losedatanan.xlsx', sheet_name='Sheet1')
lsda= pd.read_excel('losedata0.xlsx', sheet_name='Sheet1')

imp = Imputer(missing_values='NaN', strategy='most_frequent', axis=0)
imp.fit(data)
out=imp.transform(losedata)

i=0
psum=0
while(i<9):
    p=0
    p=(lsda.loc[i,'b']-out[i,1])**2/(lsda.loc[i,'b'])**2
    psum=psum+p
    #print(p)
    i=i+1
    
p=1-psum/i
print("p=",p)