import numpy as np


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
data = np.genfromtxt(url, delimiter=',', dtype='str', usecols=4)
d_s = np.sort(np.random.choice(data, size=20))

# Get unique values as a dict so we can look them up
make_dict = lambda x: dict(zip(np.unique(x), np.arange(len(x))))

# Get the data as a new list of IDs by looking up the values in the dict
d_s_u = make_dict(d_s)
r = [d_s_u[x] for x in d_s]
print(r)
