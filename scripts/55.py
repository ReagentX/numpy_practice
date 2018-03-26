import numpy as np
from scipy.stats import rankdata


a = np.random.randint(20, size=[2,5])
print('Original:')
print(a)

'''
The first `flatten()` turns the data into a single dimension array
The two `argsorts()` sort and rank the data
The `reshape()` then shapes the 1D array back to the original
'''
ranks = a.flatten().argsort().argsort().reshape(a.shape)
print('NumPy:')
print(ranks)


# Scikit
# This is 1-indexed, so we need to subtract 1 to make it zero indexed and cast as int
# This also only works across one axis, so we need to flatten and reshape as above
print('Scikit:')
rank_sp = (rankdata(a.flatten()) - 1).astype(int).reshape(a.shape)
print(rank_sp)
