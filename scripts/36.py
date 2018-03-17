import numpy as np


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# Ignore the text column since it is pesky
data = np.genfromtxt(url, delimiter=',', dtype='float', usecols=(0, 1, 2, 3))

# Use advanced indexing to pick two columns and all rows
np.corrcoef()
pwcorr = np.corrcoef(data[..., 0], data[..., 2])
print(pwcorr)
