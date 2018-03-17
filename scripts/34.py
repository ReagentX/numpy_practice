import numpy as np
import pandas as pd


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# Ignore the text column since it is pesky
data = np.genfromtxt(url, delimiter=',', dtype='float', usecols=(0, 1, 2, 3))

# Criteria uses advanced indexing
# (data[..., 2] > 1.5) means we check all rows and column 2, keeping values where the condition > 1.5 is met
filtered_data = data[(data[..., 2] > 1.5) & (data[..., 0] < 5.0)]
print(filtered_data[:5])


# Do this the right way
data_pd = pd.read_csv(url, names=['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species'])

'''
Condition `(data_pd['petallength'] > 1.5)` picks items from the data_pd column 'petallength' that satisfy the criteria
The bitwise operator ensures both conditions must be met
Criteria are in () so they are cast as tuples
'''
filtered_data_pd = data_pd[(data_pd['petallength'] > 1.5) & (data_pd['sepallength'] < 5.0)]
print(filtered_data_pd)
