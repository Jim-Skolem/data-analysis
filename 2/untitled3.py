# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 23:47:32 2017

@author: 28414
"""
import pandas as pd
from operator import add

def g(d):
    k=d[0][:]
    for l in d[1:]:
        if l[0]!=k[0]:
            yield k
            k=l
        else:
            k[1:]+map(add,l[1:],k[1:])
    yield k


data1 = pd.read_excel('totalNPdata.xlsx', sheet_name='Sheet1')
x=data1['e']
y=data1['k']

a=list(g([x,y]))
        