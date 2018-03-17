import numpy as np
import pandas as pd


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# We have to use a custom `dtype` to retain all of the data without losing any of the different formats, which means each row of data becomes a tuple
print('Downloading data...')
data = np.genfromtxt(url, delimiter=',', dtype=[float, float, float, float, object])
print('First 5 rows:')
print(data)

# The right way to do this
data_pd = pd.read_csv(url, names=['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species'])
print(data_pd.head())
