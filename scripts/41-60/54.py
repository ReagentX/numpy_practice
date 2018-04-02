import numpy as np
from scipy.stats import rankdata


np.random.seed(10)
a = np.random.randint(20, size=10)
print(list(a))

# `argsort()` works by sorting the list and returning the indexes that should go in those respectve places
# By calling it twice, we sort the indexes such that they align with the original numbers
ranks = a.argsort().argsort()
print(list(ranks))

# Scipy example
# This is 1-indexed, so we need to subtract 1 to make it zero indexed and cast as int
# This also ignores duplucates, so 9 twice gets a tie rank of 4
ranks_sp = (rankdata(a) - 1).astype(int)
print(list(ranks_sp))
