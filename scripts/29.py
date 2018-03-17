import numpy as np
import pandas as pd


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
data = np.genfromtxt(url, delimiter=',', dtype=[float, float, float, float, object])

# Take an arbitrary column from each row, make a Python list, and convert to a NumPy array
col = lambda x: np.array([row[x] for row in data])
d = col(0)
print(d[:5])

# We want to normaize everything such that the max value is 1, so we use `np.max(d)` which extracts the largest number from each row of d
d_norm = d / np.max(d)
np.set_printoptions(precision=2)
print(d_norm[:5])
