import numpy as np

a = np.arange(10)
print(a)

b = a.reshape(2, -1)  # -1 here means the width (number of columns) is variable
print(b)