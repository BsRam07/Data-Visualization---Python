import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import seaborn as sns

index = np.arange(5)
y = index**2
errorBar = index/2 # just for demonstration
plt.errorbar(index,y, yerr=errorBar, fmt='o',capsize=5, capthick=3)

plt.show()