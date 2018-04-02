import numpy as np


a = np.array([1, 2, 1, 1, 3, 4, 3, 1, 1, 2, 1, 1, 2])
v = 5

# `np.where()` generates a list of indeces where the criteria is met when args `x, y` are not passed
b = np.where(a == 1)
# Since `np.where` returns a list of tuples we need to access the first (only) item and pull the index we want (zero-indexed)
print(f'NumPy:\n{b[0][v-1]}')

# Python Example
c = [i for i, v in enumerate(a) if v == 1]
print(f'Python:\n{c[v-1]}')
