# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 12:32:31 2018

@author: 28414
"""
import pandas as pd
from sklearn.svm import LinearSVC

from sklearn.feature_selection import SelectFromModel
X = np.array(pd.read_excel('NPAndPDS.xlsx', sheet_name='Sheet1'))
y=np.array(pd.read_excel('target.xlsx', sheet_name='Sheet1'))

X.shape

lsvc = LinearSVC(C=0.01, penalty="l1", dual=False).fit(X, y)
model = SelectFromModel(lsvc, prefit=True)
X_new = model.transform(X)
X_new.shape
