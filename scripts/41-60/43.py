import numpy as np
import pandas as pd


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Get all columns as objects so we can understand the last column
data = np.genfromtxt(url, delimiter=',', dtype='object')

# The b'' means this is a byte literal
data_filtered = np.sort(data[data[..., 4] == b'Iris-setosa', [2]].astype(float))
print('NumPy')
print(f'Overall: \t{data_filtered[-2]}')

# Since the exercise uses the secnd largest unique value
print(f'Unique: \t{np.unique(data_filtered)[-2]}')

# Pandas example
data_pd = pd.read_csv(url, names=['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species'])

# Get the data where the `species` column is `Iris-setosa` using advanced indexing
data_filtered_pd = data_pd[data_pd['species'] == 'Iris-setosa']
# Sort the values on the `petallength` column
data_sorted_pd = data_filtered_pd.sort_values('petallength')
# Get the values as an `ndarray`
data_sorted_filtered = data_sorted_pd['petallength'].values

print('Pandas')
print(f'Overall: \t{data_sorted_filtered[-2]}')

# Since the exercise uses the secnd largest unique value
print(f'Unique: \t{np.unique(data_sorted_filtered)[-2]}')
