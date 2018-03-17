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

# Real normalization might have messy data, so we need to check for negatives
def check_norm(x):
    '''Returns True if the normalization is between 0 and 1 else False'''
    return True if len(x[(x < 0) ^ (x > 1)]) == 0 else False

print('Normalization success' if check_norm(d_norm) else 'Normalization failiure')

# Do this the right way
data_pd = pd.read_csv(url, names=['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species'])
# Access the proper column using the name `data_pd['species']`
d_pd = data_pd['sepallength']
d_pd_norm = d_pd/d_pd.max()
print(d_pd_norm.head())
print('Normalization success' if check_norm(d_pd_norm) else 'Normalization failiure')
