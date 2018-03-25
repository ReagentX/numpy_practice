import numpy as np
from collections import Counter


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Get all columns as objects so we can understand the last column
data = np.genfromtxt(url, delimiter=',', dtype='object')

# Pure python
print(Counter(data[..., 2]).most_common(1))

# NumPy
# Using `return_counts=True` also returns the counts of the unique values
vals, counts = np.unique(data[..., 2], return_counts=True)
# `np.argmax(counts)` returns the index of the position that is the largest in `counts`
print(f'[({vals[np.argmax(counts)]}, {max(counts)})]')
