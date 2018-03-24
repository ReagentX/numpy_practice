import numpy as np
import pandas as pd
from scipy.stats.stats import pearsonr


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# Ignore the text column since it is pesky
data = np.genfromtxt(url, delimiter=',', dtype='float', usecols=(0, 1, 2, 3))

# Use advanced indexing to pick two columns and all rows
corr = np.corrcoef(data[..., 0], data[..., 3])
np.set_printoptions(precision=2)
print(f'NumPy:\t{corr[0, 1]:.3f}')

# Do this the right way
data_pd = pd.read_csv(url, names=['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species'])

corr_pd = data_pd['sepallength'].corr(other=data_pd['petalwidth'])
print(f'Pandas:\t{corr_pd:.3f}')

# Another right way
corr_sp = pearsonr(data_pd['sepallength'], data_pd['petalwidth'])
print(f'SciPy:\t{corr_sp[0]:.3f}, p = {corr_sp[1]:.3f}')
