# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 21:48:46 2018

@author: 28414
"""

import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import matplotlib.pyplot as plt

#数据
X = np.array(pd.read_excel('NPAndPDS.xlsx', sheet_name='Sheet1'))
y=np.array(pd.read_excel('target.xlsx', sheet_name='Sheet1'))
print("原数据大小：",X.shape)

sk = SelectKBest(chi2, k=18)
X_new = sk.fit_transform(X, y)
scores=sk.scores_

print("特征选择后的大小：",X_new.shape)
#print("每个特征的得分：",list(scores))
plt.plot(scores)
plt.title("the socores of every featrue")