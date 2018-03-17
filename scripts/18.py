import numpy as np


a = np.arange(9).reshape(3,3)
print(a)

# Advanced indexing using a[rows, columns]
# The ... means that we include the entire number of dimensions for the specific part of the array
b = a[::-1, ...]
print(b)
