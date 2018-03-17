import numpy as np


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
data = np.genfromtxt(url, delimiter=',', dtype=[float, float, float, float, object])

# Take the fourth column `row[4]` from each row, make a Python list, and convert to a NumPy array
col = lambda x: np.array([row[x] for row in data])
d = col(0)
print(f'NumPy\tMean: {np.mean(d):.2f}, Median: {np.median(d):.2f}, Sigma: {np.std(d):.2f}')
