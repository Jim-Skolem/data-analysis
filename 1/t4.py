import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_style("whitegrid")
data1 = pd.read_excel('totalNPdata.xlsx', sheet_name='Sheet1')
data2 = pd.read_excel('totalPDSdat.xlsx', sheet_name='Sheet1')
ax = sns.barplot(x="height", y="steps", data=data1,ci=0)
plt.show();