import numpy as np


arr1 = np.arange(3)
arr2 = np.arange(3,7)
arr3 = np.arange(7,10)

a = np.array([arr1, arr2, arr3])
print(a)

# Horizontally "stack" all of the arrays
b = np.hstack(a)
print(b)
