import numpy as np


a = np.array([1,2,3,4,5])
b = np.array([4,5,6,7,8])

# NumPy Example using Linear Algebra
d_np = np.linalg.norm(a-b)
print(f'{d_np:.3f}')
