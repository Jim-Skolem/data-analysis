# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:23:57 2017

@author: 28414
"""

import matplotlib.pyplot as plt
import scipy.io as scio
import numpy as np

def ma(list2):
    n = len(list2)
    sum = 0
    for i in list2:
        sum += i
    result = sum / n
    return result

def answer1(list1, n):    
    listMA = []  
    for i in range(n - 1, len(list1)):        
        list2 = (list1[i - (n - 1):i + 1])
        listMA.append(ma(list2))
   
    plt.plot(list(range(len(listMA))), listMA,linewidth=2,color='k')
    plt.show()

if __name__ == '__main__':
    data = scio.loadmat('NP01_1.mat')

    d1=data['NP01_1_data']
    b=d1.sum(axis=1)
    c=b.sum(axis=1)
    x = np.linspace(0,441,442)    
    y=c
    
    plt.plot(x,y,linewidth=2,color='g')    
    answer1(y, 10)  
