import numpy as np
import pandas as pd


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
data = np.genfromtxt(url, delimiter=',', dtype='object')

# Store the rows and columns as a numpy array
row, col = np.where(data)

'''
`data[row, col] = x` will assign x to the value in [row, col]
`np.random.choice((row), 100)` chooses a random row (and using `col` chooses a column) 100 times
This uses advanced indexing to iterate through the numpy array `data` and replaces items with `np.nan`
'''
data[np.random.choice((row), 100), np.random.choice((col), 100)] = np.nan
print(data[:5])
