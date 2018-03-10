import numpy as np

a = np.array([[True for x in range(3)] for x in range(3)])
b = np.full((3, 3), True, dtype=bool)

print(a)
print(b)