import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import seaborn as sns

# Generate the data
x = np.random.randn(500)
#x = pd.read_csv('data1.txt', delimiter='[ ,]*')
# Plot-command start ---------------------

plt.plot(stats.cumfreq(x,)[0])
# Plot-command end -----------------------

# Show plot
plt.show()