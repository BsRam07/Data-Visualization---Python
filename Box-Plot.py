import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import seaborn as sns

x = np.arange(5)

plt.boxplot(x, sym='*')

plt.show()