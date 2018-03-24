import numpy as np


np.random.seed(100)
a = np.random.random([3,3])/1e3
print(a)

# Supress is not noted in the documentation (https://docs.scipy.org/doc/numpy/reference/generated/numpy.set_printoptions.html)
# It disables printing of scientific notation
np.set_printoptions(suppress=True)
print(a)
