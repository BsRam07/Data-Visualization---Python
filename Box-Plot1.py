import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import seaborn as sns

# Generate the data
nd = stats.norm
data = nd.rvs(size=(100))
nd2 = stats.norm(loc = 3, scale = 1.5)
data2 = nd2.rvs(size=(100))
# Use pandas and the seaborn package
# for the violin plot
df = pd.DataFrame({'Girls':data, 'Boys':data2})
sns.violinplot(df)