import numpy as np


a = np.arange(11)
b = np.arange(11)
print(a)
print(b)

a = filter(lambda x: x % 2 == 1, a)  # Keep values where `x % 2 == 1`
b = b[b % 2 == 1]
print(a)
print(b)
