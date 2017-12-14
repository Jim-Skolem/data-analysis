# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:31:50 2017

@author: 28414
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data1 = pd.read_excel('totalNPdata.xlsx', sheet_name='Sheet1')
data2 = pd.read_excel('totalPDSdat.xlsx', sheet_name='Sheet1')

leftsteps=data1['e'].values.transpose()
rightsteps=data1['m'].values.transpose()

plt.stackplot(leftsteps,rightsteps)

