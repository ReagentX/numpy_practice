import numpy as np


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# Ignore the text column since it is pesky
data = np.genfromtxt(url, delimiter=',', dtype='float', usecols=(0, 1, 2, 3))

row, col = np.where(data)
# Replace 5 random [row, col] pairs with `np.nan`
data[np.random.choice((row), 5), np.random.choice((col), 5)] = np.nan

# np.argwhere finds the [row, col] pairs where the argument criteria is met
nan_places = np.argwhere(np.isnan(data))
print(nan_places)
