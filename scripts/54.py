import numpy as np


np.random.seed(10)
a = np.random.randint(20, size=10)
print(list(a))

# `argsort()` works by sorting the list and returning the indexes that should go in those respectve places
# By calling it twice, we sort the indexes such that they align with the original numbers
r = a.argsort().argsort()
print(list(r))
