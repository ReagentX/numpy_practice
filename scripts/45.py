import numpy as np
import pandas as pd
from collections import Counter


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Get all columns as objects so we can understand the last column
data = np.genfromtxt(url, delimiter=',', dtype='float')

# Pure python
print(f'Python:\t{Counter(data[..., 2]).most_common(1)[0]}')

# NumPy
# Using `return_counts=True` also returns the counts of the unique values
vals, counts = np.unique(data[..., 2], return_counts=True)
# `np.argmax(counts)` returns the index of the position that is the largest in `counts`
print(f'NumPy:\t{vals[np.argmax(counts)]}, {max(counts)}')

# Pandas
data_pd = pd.read_csv(url, names=['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species'])

# Get the unique value counts
uniques = data_pd['petallength'].value_counts()
print(f'Pandas:\t{uniques.index[0]}, {uniques.iloc[0]}')
