import numpy as np


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
data = np.genfromtxt(url, delimiter=',', dtype=[float, float, float, float, object])

# Take an arbitrary column from each row, make a Python list, and convert to a NumPy array
col = lambda x: np.array([row[x] for row in data])
d = col(0)
print(d[:5])

# Softmax function
def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=0)

np.set_printoptions(precision=3)
print(f'Softmax score {softmax(d)}')
