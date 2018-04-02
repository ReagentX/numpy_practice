import numpy as np


np.random.seed(100)
a = np.random.uniform(1,50, 20)

# Sort the array
b = np.sort(a)

# Get the last 5 items
print(b[-5:])
