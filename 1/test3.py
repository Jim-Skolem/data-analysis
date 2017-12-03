import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set_style("whitegrid")

data1 = pd.read_excel('totalNPdata.xlsx', sheet_name='Sheet1')
data2 = pd.read_excel('totalPDSdat.xlsx', sheet_name='Sheet1')

ax = sns.boxplot(x="sex", y="height", data=data2)

plt.show();