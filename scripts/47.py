import numpy as np

low = 10
high = 30
check = lambda a, l, h: [x for x in a if x > h or x < l]

np.random.seed(100)
a = np.random.uniform(1, 50, 20)
print(a)
print('Numbers are out of range.' if check(a, low, high) else 'Numbers in range!')

b = np.clip(a, 10, 30)
print(b)
print('Numbers are out of range.' if check(b, low, high) else 'Numbers in range!')
