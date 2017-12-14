# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 21:40:19 2017

@author: 28414
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data1 = pd.read_excel('totalNPdata.xlsx', sheet_name='Sheet1')
data2 = pd.read_excel('totalPDSdat.xlsx', sheet_name='Sheet1')
x=data1['e']
y=data1['k']
z=data1['h']
a=data2['e']
b=data2['k']
c=data2['h']

plt.figure(figsize=(10,10)) 
plt.subplot(221)
plt.xlabel('buchang')
plt.ylabel('baidongshijian')
plt.scatter(x,y,c='c',marker=".")
fp1 = np.polyfit(x,y,3)
f1 = np.poly1d(fp1)
fx = np.linspace(min(x),max(x),1000)
plt.plot(fx,f1(fx),linewidth=2,color='k')
plt.subplot(222)
plt.xlabel('busu')
plt.ylabel('baidongshijian')
plt.scatter(z,y,c='c',marker="x")
fp2 = np.polyfit(z,y,3)
f2 = np.poly1d(fp2)
fz = np.linspace(min(z),max(z),1000)
plt.plot(fz,f2(fz),linewidth=2,color='k')
plt.subplot(223)
plt.xlabel('buchang')
plt.ylabel('baidongshijian')
plt.scatter(a,b,c='c',marker=".")
fp3 = np.polyfit(a,b,3)
f3 = np.poly1d(fp3)
fa = np.linspace(min(a),max(a),1000)
plt.plot(fa,f3(fa),linewidth=2,color='k')
plt.subplot(224)
plt.xlabel('busu')
plt.ylabel('baidongshijian')
plt.scatter(c,b,c='c',marker="x")
fp4 = np.polyfit(c,b,3)
f4 = np.poly1d(fp4)
fc = np.linspace(min(c),max(c),1000)
plt.plot(fc,f4(fc),linewidth=2,color='k')
plt.show()

"""
a=[1,2,3,4]
b=[2,5,6,8]
#plt.ylim((300,600))
#plt.yticks(np.linspace(300, 1000, 12))
plt.savefig('lena_new_sz.png')

plt.subplot(212)
plt.scatter(x,z,c='k',marker="x")
fp3 = np.polyfit(x,z,3)
f3 = np.poly1d(fp3)
plt.plot(fx,f3(fx),linewidth=2,color='b')
plt.show()
"""