import numpy as np


a = np.random.randint(10, size=10)
print(a)

# Python example
stride = 3  # Moving average includes `stride + 1` since arrays are zero indexed
p_avg = [a[i:i + stride].sum()/(stride) for i, v in enumerate(a)]
print(p_avg)

# As a function
def moving_average(a, s):
    return [a[i:i + s].sum()/(s) for i, v in enumerate(a)]


print(moving_average(a, 3))
