from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

arr = np.random.normal(size=100)

# plot histogram
plt.subplot(221)
plt.hist(arr)

# obtain histogram data
plt.subplot(222)
hist, bin_edges = np.histogram(arr)
plt.plot(hist)

# fit histogram curve
plt.subplot(223)
sns.distplot(arr, kde=False, fit=stats.gamma, rug=True)
plt.show()