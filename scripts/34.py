import numpy as np


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# Ignore the text column since it is pesky
data = np.genfromtxt(url, delimiter=',', dtype='float', usecols=(0, 1, 2, 3))

# Criteria uses advanced indexing
# (data[..., 2] > 1.5) means we check all rows and column 2, keeping values where the condition > 1.5 is met
filtered_data = data[(data[..., 2] > 1.5) & (data[..., 0] < 5.0)]
print(filtered_data[:5])
