import numpy as np


a = np.random.randint(1, 20, [5, 3])
print(a)

'''
Using NumPy
We specify `axis=1` to operate in terms of rows and not columns
This is the better solution because it can also work for columns
'''
a_n = np.amax(a, axis=1)
print(a_n)

# Using dictionary comprehension (keep index)
a_d = {i: max(a) for i, a in enumerate(a)}
print(a_d)

# Using list comprehension (ignore index)
a_l = [max(i) for i in a]
print(a_l)
