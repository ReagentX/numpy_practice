import numpy as np


a = np.arange(9999)

# Set the threshold with which to cut off arrays to infinity
np.set_printoptions(threshold=np.inf)
print(a)