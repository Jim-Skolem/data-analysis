# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 22:47:11 2017

@author: 28414
"""

import scipy.io as scio
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

data = scio.loadmat('NP01_1.mat')

d1=data['NP01_1_data']
d2=data['NP01_1_cut']

b=d1.sum(axis=1)
c=b.sum(axis=1)
x = np.linspace(0,441,442)
y=c

plt.plot(x,y,linewidth=2,color='k')
