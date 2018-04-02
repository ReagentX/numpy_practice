import numpy as np


a = np.array([1, 3, 7, 1, 2, 6, 0, 1])

# Pure Python
b = []
for i, v in enumerate(a):
    if a[max(i-1, 0)] < v and a[min(len(a)-1, i+1)] < v:
        b.append(i)

print(b)
