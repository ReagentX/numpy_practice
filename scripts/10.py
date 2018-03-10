import numpy as np


a = np.arange(1, 4)
print(a)

# np.repeat(a, n) repeats each element of a `n` times
# np.tile tiles a `n` times
# np.r_ stacks arrays along the first axis, aka the first element in a array
a = np.r_[np.repeat(a, 3), np.tile(a, 3)]
print(a)