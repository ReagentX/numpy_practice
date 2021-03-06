import numpy as np
import pandas as pd


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Get all columns as floats since we ignore the last column
data = np.genfromtxt(url, delimiter=',', dtype='object')
print('NumPy:')

# The actual datapoint without the position using advanced indexing
data_filtered = data[data[..., 3].astype(float) > 1.0]
print(data_filtered[0])
# The position, given by np.argwhere()
data_position = np.argwhere(data[..., 3].astype(float) > 1.0)
print(data_position[0])

# Pandas Example
data_pd = pd.read_csv(url, names=['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species'])

data_filtered = data_pd[data_pd['petalwidth'] > 1.0]
print('\nPandas:')
print(data_filtered.iloc[0])
