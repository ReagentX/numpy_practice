import numpy as np
from scipy.spatial import distance


a = np.array([1,2,3,4,5])
b = np.array([4,5,6,7,8])

# NumPy Example using Linear Algebra
d_np = np.linalg.norm(a-b)
print(f'NumPy:\n{d_np:.3f}')

# Scipy example (only works with 1D arrays)
d_sp = distance.euclidean(a, b)
print(f'Scipy:\n{d_sp:.3f}')
