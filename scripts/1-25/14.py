import numpy as np


a = np.arange(15)

b = np.where((a >= 5) & (a <= 10))
print(b[0])