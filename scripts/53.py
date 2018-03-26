import numpy as np


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
data = np.genfromtxt(url, delimiter=',', dtype='str', usecols=4)
d_s = np.sort(np.random.choice(data, size=20))

# Get unique values as a dict
d_s_u = dict(zip(np.unique(d_s), np.arange(len(d_s))))

# Get the data as a new list of IDs
r = [d_s_u[x] for x in d_s]
print(r)
