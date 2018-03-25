import numpy as np
import pandas as pd


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Get all columns as objects so we can understand the last column
data = np.genfromtxt(url, delimiter=',', dtype='object')

# Get the species separately so we can sample
all_species = data[..., [4]]
unique_species = np.unique(all_species)

# Distribute species in the proper ratios over n samples
n = 100  # The number of samples
p = [0.25, 0.25, 0.5]  # The weights for each sample
species_distributed = np.random.choice(unique_species, n, p=p)

# Print the number of each species
print('NumPy:')
for s in unique_species:
    print(f'{s}: \t{len([x for x in species_distributed if x == s])}')

# The right way to do this
data_pd = pd.read_csv(url, names=['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species'])

# Sample based on weights from the species column
print('Pandas:')
p_pd = {'Iris-setosa': 0.25, 'Iris-versicolor': 0.25, 'Iris-virginica': 0.5}  # The weights for each sample

# Generate relative sizes to sample the proper number based on the number of samples using dict compression
# `len(data_pd[data_pd['species'] == x]` gets the column `data_pd['species']` and uses advanced indexing to get those that match `p_pd`
sizes = {x: (p_pd[x] * n) / len(data_pd[data_pd['species'] == x]) for x in p_pd}

'''
Group by species and select only the species column, then apply a function to each group
The function samples each group and uses the weight in the dict by looking up the key `s.unique()[0]`
This means it generates the number of unique values in the group (there is one since we pull the category only)
'''
species_distributed_pd = data_pd.groupby('species')['species'].apply(lambda s: s.sample(frac=sizes[s.unique()[0]]))
print(species_distributed_pd.value_counts())
