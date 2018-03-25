import numpy as np
import pandas as pd


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Get all columns as objects so we can understand the last column
data = np.genfromtxt(url, delimiter=',', dtype='object')

data_sorted = data[data[:, 0].argsort()]
print(data_sorted[::25])

# Pandas example
data_pd = pd.read_csv(url, names=['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species'])

# Sort the data by the `sepallength` column
data_sorted_pd = data_pd.sort_values('sepallength')
print(data_sorted_pd[::25])
