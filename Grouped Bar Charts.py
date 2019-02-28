import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import seaborn as sns

df = pd.DataFrame(np.random.rand(10, 4),columns=['a', 'b', 'c', 'd'])

df.plot(kind='bar', grid=False)

plt.show()