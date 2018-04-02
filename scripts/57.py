import numpy as np


a = np.random.randint(1, 20, [5, 3])
np.set_printoptions(precision=2)
print(a)

# Using NumPy
# `apply_along_axis()` allows us to apply a function across a defined axis of a NumPy array
min_by_max = np.apply_along_axis(lambda x: min(x)/max(x), arr=a, axis=1)
print(min_by_max)
