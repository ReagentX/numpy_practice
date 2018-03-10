import numpy as np

a = np.arange(10)
print(a)

b = np.where(a % 2 == 1, -1, a)  # Takes each element from `a`, applies the condition, then places the proper value in a new array
print(a)
print(b)