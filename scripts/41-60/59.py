import numpy as np
import pandas as pd


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Get all columns as objects, we will need to convert to do math
data = np.genfromtxt(url, delimiter=',', dtype='object')
print('NumPy:')

# Loop through all of the unique values
for i in np.unique(data[..., 4]):
    # Use advanced indexing to pull column [1] from the rows where column 4 is i
    print(f'{i.decode()}:\t{data[data[..., 4] == i, [1]].astype(float).mean():.3f}')

# Pandas example
data_pd = pd.read_csv(url, names=['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species'])

# Specifying `['sepalwidth']` means we ignore the other columns
print('Pandas:')
print(data_pd.groupby(['species'])['sepalwidth'].mean())
