import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import seaborn as sns

txtLabels = 'Cats', 'Dogs', 'Frogs', 'Others' 
fractions = [45, 30, 15, 10]
offsets =(0, 0.05, 0, 0)
plt.pie(fractions, explode=offsets, labels=txtLabels,autopct='%1.1f%%', shadow=True, startangle=90,colors=sns.color_palette('muted') )
plt.axis('equal')
plt.show()