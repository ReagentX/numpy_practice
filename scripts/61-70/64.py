import numpy as np


a = np.array([[3,3,3],[4,4,4],[5,5,5]])
b = np.array([1, 2, 3])

# None here converts `b` into a 2D array by adding a dimension full of `None`
c = a - b[..., None]
print(c)
