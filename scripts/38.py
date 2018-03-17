import numpy as np


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# Ignore the text column since it is pesky
data = np.genfromtxt(url, delimiter=',', dtype='float', usecols=(0, 1, 2, 3))

# False if there are no np.nan elements present
validate = lambda x: np.isnan(x).any()

# Generate an array of rows and columns
row, col = np.where(data)

# Replace 120 random [row, col] pairs with `np.nan`
data[np.random.choice((row), 120), np.random.choice((col), 120)] = np.nan
print(data[:5])

# Use advanced slicing to find all of the indexes of `np.nan` and set them to 0
data[np.isnan(data)] = 0
print(data[:5])
