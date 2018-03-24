import numpy as np


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Get all columns as objects so we can understand the last column
data = np.genfromtxt(url, delimiter=',', dtype='object')

# Get the species separately so we can sample
all_species = data[..., [4]]
unique_species = np.unique(all_species)

# Distribute species in the proper ratios over n samples
n = 25
species_distributed = np.random.choice(unique_species, n, p=[0.25, 0.25, 0.5])

# Print the number of each species
print('NumPy:')
for s in unique_species:
    print(f'{s}: {len([x for x in species_distributed if x == s])}')
