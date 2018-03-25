import numpy as np


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Get all columns as objects so we can understand the last column
data = np.genfromtxt(url, delimiter=',', dtype='object')

# The b'' means this is a byte literal
data_filtered = np.sort(data[data[..., 4] == b'Iris-setosa', [2]].astype(float))
print(f'Overall: \t{data_filtered[-2]}')

# Since the exercise uses the secnd largest unique value
print(f'Unique: \t{np.unique(data_filtered)[-2]}')
