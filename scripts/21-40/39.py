import numpy as np
import pandas as pd


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
data = np.genfromtxt(url, delimiter=',', dtype=[float, float, float, float, object])

# Take an arbitrary column from each row, make a Python list, and convert to a NumPy array
col = lambda x: np.array([row[x] for row in data])

species = np.unique(col(4))
print(f'{len(species)} species.')


# The right way to do this
data_pd = pd.read_csv(url, names=['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species'])

# Find the number of unique items in the species column
species_num = data_pd['species'].nunique()

# Find the number each unique item shows up
species_pd = data_pd['species'].value_counts()

print(f'{species_num} species.')
print(species_pd)
