import pandas as pd
import numpy as np

data = np.loadtxt('data.txt', delimiter=',') 
print(data)

df = pd.read_csv('data.txt', header=None)
print(df)
print('\n')
df1 = pd.read_csv('data.txt')
print(df1)