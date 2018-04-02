import numpy as np
import pandas as pd
import math


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# Ignore the text column since it is pesky
data = np.genfromtxt(url, delimiter=',', dtype='float', usecols=(0, 1, 2, 3))

# Take an arbitrary column from each row, make a Python list, and convert to a NumPy array
col = lambda x, d: np.array([row[x] for row in d])

# Get the respective columns as NumPy arrays
sepallength = col(0, data)
petallength = col(2, data)

# Calculate volume, transform, append
vol = ((math.pi * petallength * sepallength ** 2) / 3)[:, np.newaxis]
data = np.hstack([data, vol])

np.set_printoptions(precision=3, suppress=True)
print(data[::25])

# The right way to do this
data_pd = pd.read_csv(url, names=['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species'])
data_pd['volume'] = ((math.pi * data_pd['petallength'] * data_pd['sepallength'] ** 2) / 3)

print(data_pd[::25])
