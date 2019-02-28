import numpy as np
import pandas as pd
t = np.arange(0,10,0.1)
x = np.sin(t)
y = np.cos(t)
df = pd.DataFrame({'Time':t, 'x':x, 'y':y})

data = df[['Time', 'y']]
#print(data)

h1 = data.head()
t1 = data.tail()

#print(t1)
#print(h1)
 	
#To extract the six rows from 5 to 10, use
print(data[4:10])
