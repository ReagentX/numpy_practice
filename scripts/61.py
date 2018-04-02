import numpy as np


a = np.array([1, 2, 3, np.nan, 5, 6, 7, np.nan])
print(a)

# Using NumPy
# ~ is shorthand for a logical not in NumPy since we cannot do a normal `not` here
b = a[~np.isnan(a)]
print(b)

# Using list comprehension 
# Cast x as int for readability
b_c = [int(x) for x in a if not np.isnan(x)]
print(b_c)
