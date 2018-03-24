import numpy as np


a = np.arange(9999)
print(a)

# Set the threshold to truncate to infinity
np.set_printoptions(threshold=np.inf)
print(a)