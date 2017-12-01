import numpy as np
import statsmodels.api as sm # recommended import according to the docs
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data1 = pd.read_excel('totalNPdata.xlsx', sheet_name='Sheet1')
data2 = pd.read_excel('totalPDSdat.xlsx', sheet_name='Sheet1')
ecdf = sm.distributions.ECDF(data2['weight'])

x = np.linspace(min(data2['weight']), max(data2['weight']))
y = ecdf(x)
#plt.step(x, y)
plt.hist(data2['weight'], bins=50, color='steelblue', normed=True )
plt.show()