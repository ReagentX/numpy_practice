import numpy as np


a = np.random.randint(20, size=[2,5])
print(a)

'''
The first `flatten()` turns the data into a single dimension array
The two `argsorts()` sort and rank the data
The `reshape()` then shapes the 1D array back to the original
'''
ranks = a.flatten().argsort().argsort().reshape(a.shape)
print(ranks)
