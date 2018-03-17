import numpy as np
import pandas as pd


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# Ignore the text column since it is pesky
data = np.genfromtxt(url, delimiter=',', dtype='float', usecols=(0, 1, 2, 3))

# Use advanced indexing to pick two columns and all rows
corr = np.corrcoef(data[..., 0], data[..., 3])
np.set_printoptions(precision=2)
print(f'{corr[0, 1]:.3f}')

# Do this the right way
data_pd = pd.read_csv(url, names=['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species'])

corr_pd = data_pd['sepallength'].corr(other=data_pd['petalwidth'])
print(f'{corr_pd:.3f}')
