# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 12:07:48 2018

@author: 28414
"""

import pandas as pd
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectFromModel

#数据
X = np.array(pd.read_excel('NPAndPDS.xlsx', sheet_name='Sheet1'))
y=np.array(pd.read_excel('target.xlsx', sheet_name='Sheet1'))

print("原数据大小：",X.shape)

lsvc = LinearSVC(C=0.01, penalty="l1", dual=False).fit(X, y)
model = SelectFromModel(lsvc, prefit=True)
X_new = model.transform(X)

print("特征选择后的大小：",X_new.shape)
