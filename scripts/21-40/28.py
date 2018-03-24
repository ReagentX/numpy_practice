import numpy as np
import pandas as pd


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
data = np.genfromtxt(url, delimiter=',', dtype=[float, float, float, float, object])

# Take an arbitrary column from each row, make a Python list, and convert to a NumPy array
col = lambda x: np.array([row[x] for row in data])
d = col(0)
print(f'NumPy\tMean: {np.mean(d):.2f}, Median: {np.median(d):.2f}, Sigma: {np.std(d):.2f}')

# The right way to do this
data_pd = pd.read_csv(url, names=['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species'])
# Access the proper column using the name `data_pd['species']`
d_pd = data_pd['sepallength']
print(f'Pandas\tMean: {d_pd.mean():.2f}, Median: {d_pd.median():.2f}, Sigma: {d_pd.std():.2f}')
