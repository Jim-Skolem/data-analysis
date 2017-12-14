# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 12:14:54 2017

@author: 28414
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as scio

data = scio.loadmat('PD01_1.mat')

d1=data['PD01_1_data']
b=d1.sum(axis=1)
c=b.sum(axis=1)
x = np.linspace(0,838,839)    
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