import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import seaborn as sns

sns.set()
df = sns.load_dataset("iris")
sns.pairplot(df, hue="species", size=2.5)
plt.show()