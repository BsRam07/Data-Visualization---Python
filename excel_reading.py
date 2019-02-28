import pandas as pd
import numpy as np

#df2 = pd.read_csv('data1.txt', delimiter='[ ,]*')

xls = pd.ExcelFile('excel_data.xls')
data = xls.parse('Sheet1', index_col=None, na_values=['NA'])

# using the read_excel function
data = pd.read_excel('excel_data.xls', 'Sheet1',
index_col=None, na_values=['NA'])

print(data)