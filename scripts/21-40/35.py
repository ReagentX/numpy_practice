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
print('np.nan present' if validate(data) else 'np.nan removed')

# Find out the indexes of all of the `np.nan`s as [row, col]
nans = np.argwhere(np.isnan(data))

# Delete all of the rows in data, specify `axis=0` so we do not flatten and instead work on the rows separately
data_clean = np.delete(data, nans[..., 0], axis=0)
print(data_clean[:5])
print('np.nan present' if validate(data_clean) else 'np.nan removed')
