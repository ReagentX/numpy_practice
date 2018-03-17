import numpy as np


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Remove the last dtype to omit
data = np.genfromtxt(url, delimiter=',', dtype=[float, float, float, float])

print(data[:5])