import numpy as np
import pandas as pd


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
data = np.genfromtxt(url, delimiter=',', dtype=[float, float, float, float, object])

# Take an arbitrary column from each row, make a Python list, and convert to a NumPy array
col = lambda x: np.array([row[x] for row in data])
d = col(0)
print(d[:5])

# Get the 10th and 95th percentiles
d_percentiles = np.percentile(d, [10, 95])
np.set_printoptions(precision=2)
print(d_percentiles)

# Do this the right way
data_pd = pd.read_csv(url, names=['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species'])
d_pd = data_pd['sepallength']

print(f'[{d_pd.quantile(0.1):.2f} {d_pd.quantile(0.95):.2f}]')