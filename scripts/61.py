import numpy as np


a = np.array([1, 2, 3, np.nan, 5, 6, 7, np.nan])
print(a)

# Using NumPy
# ~ is shorthand for a logical not in NumPy since we cannot do a normal `not` here
b = a[~np.isnan(a)]
print(b)
