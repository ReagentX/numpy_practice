import numpy as np


a = np.arange(9).reshape(3,3)
print(a)

# Advanced indexing using a[rows, columns] where we swap columns 0 and 1 statically
# The ... means that we include the entire number of dimensions for rows and then only index the columns
b = a[..., [1, 0, 2]]
print(b)
