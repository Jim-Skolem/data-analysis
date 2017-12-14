# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:48:02 2017

@author: 28414
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as scio

data = scio.loadmat('NP01_1.mat')

d1=data['NP01_1_data']
b=d1.sum(axis=1)
c=b.sum(axis=1)
x = np.linspace(0,441,442)    
y=c

plt.figure(figsize=(10,10)) 

plt.subplot(211)
moving_avg = pd.rolling_mean(y,2)
plt.plot(y)
plt.plot(moving_avg, color='red')

plt.subplot(212)
expwighted_avg = pd.ewma(y, halflife=2)
plt.plot(y)
plt.plot(expwighted_avg, color='red')