import numpy as np


a = np.random.random((5,3))
print(a)

# Set the precision at which to print floats
np.set_printoptions(precision=3)
print(a)