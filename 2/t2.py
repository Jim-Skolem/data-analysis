# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 23:15:08 2017

@author: 28414
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data1 = pd.read_excel('totalNPdata.xlsx', sheet_name='Sheet1')
data2 = pd.read_excel('totalPDSdat.xlsx', sheet_name='Sheet1')
x1=data1['e']
y1=data1['m']
x2=data2['e']
y2=data2['m']

plt.figure(figsize=(6,6)) 
plt.subplot(111)
plt.xlabel('zuobuchang')
plt.ylabel('youbuchang')
plt.scatter(x1,y1,c='c',marker=".")
fp1 = np.polyfit(x1,y1,3)
f1 = np.poly1d(fp1)
fx1 = np.linspace(min(x1),max(x1),1000)
plt.plot(fx1,f1(fx1),linewidth=2,color='k')
plt.show()
plt.figure(figsize=(6,6))
plt.subplot(111)
plt.xlabel('zuobuchang')
plt.ylabel('youbuchang')
plt.scatter(x2,y2,c='b',marker="x")
fp2 = np.polyfit(x2,y2,3)
f2 = np.poly1d(fp2)
fx2 = np.linspace(min(x2),max(x2),1000)
plt.plot(fx2,f1(fx2),linewidth=2,color='k')
plt.show()


"""
for kind in ['nearest', 'zero', 'linear', 'quadratic', 'cubic']:
    plt.plot(x, y, label=kind)
    
    
    
    
plt.subplot(212)
plt.xlabel('zuobuchang')
plt.ylabel('youbuchang')
fx = np.linspace(min(x),max(x),1000)
plt.plot(fx,f2(fx),linewidth=2,color='k')
"""