#coding=utf-8

import pandas as pd
from scipy import stats, integrate
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white", palette="muted", color_codes=True)
rs = np.random.RandomState(10)

f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)
sns.despine(left=True)

data1 = pd.read_excel('totalNPdata.xlsx', sheet_name='Sheet1')
data2 = pd.read_excel('totalPDSdat.xlsx', sheet_name='Sheet1')


sns.distplot(data2['steps'], kde=False, color="b", ax=axes[0, 0])
sns.distplot(data2['steps'], hist=False, rug=True, color="r", ax=axes[0, 1])
sns.distplot(data2['steps'], hist=False, color="g", kde_kws={"shade": True}, ax=axes[1, 0])
sns.distplot(data2['steps'], color="m", ax=axes[1, 1])

plt.setp(axes, yticks=[])
plt.tight_layout()

plt.show();


'''
x = data1['age']
sns.distplot(x, kde=True, rug=True)
plt.show()

data1['age'].plot()
plt.ylabel('some numbers')  #为y轴加注释
plt.show()

plt.figure('weight1')
ax1=sns.stripplot(x=data1['weight'],jitter=True)
ax1.set_title('normal')

plt.figure('weight2')
ax2=sns.stripplot(x=data2['weight'],jitter=True)
ax2.set_title('patient')
plt.show();
'''


