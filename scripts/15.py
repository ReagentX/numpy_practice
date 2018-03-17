import numpy as np


def maxx(x, y):
    return x if x >= y else y


vmaxx = np.vectorize(maxx)

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

c = vmaxx(a, b)
print(c)
