import numpy as np


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# Ignore the text column since it is pesky
data = np.genfromtxt(url, delimiter=',', dtype='float', usecols=(0, 1, 2, 3))

# .any() means we check if any element of `data` is `np.nan`
# True if there are no np.nan elements present
validate = lambda x: not np.isnan(x).any()
print('No missing values' if validate(data) else 'Missing values detcted')
