import numpy as np

low = 10
high = 30
check = lambda a, l, h: print('Numbers are out of range.' if [x for x in a if x > h or x < l] else 'Numbers in range!')
np.set_printoptions(precision=2)

np.random.seed(100)
a = np.random.uniform(1, 50, 20)
print(a)
check(a, low, high)

b = np.clip(a, 10, 30)
print(b)
check(b, low, high)
