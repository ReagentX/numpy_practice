import numpy as np


a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

# Creates a new array with the common items after sorting (low to high)
c = np.intersect1d(a, b)
print(c)

# This does the same thing as the above function call
d = np.array(sorted(list(set([x for x in a if x in b]))))
print(d)