import numpy as np


a = np.random.randint(1, 20, [5, 3])
print(a)

'''Using NumPy
We specify `axis=1` to operate in terms of rows and not columns
This is the better solution because it can also work for columns
'''
a_n = np.amax(a, axis=1)
print(a_n)
