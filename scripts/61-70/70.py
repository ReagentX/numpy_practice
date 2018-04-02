import numpy as np


a = np.arange(15)
print(a)

def gen(a, w, s):
    # Determine the number of sub-arrays (aka rows) we make with the given window (row) size using floor divison
    stride = ((a.size - w) // s) + 1

    # This takes the stride and generates an array starting at zero containing the first entry's in the main array index in each row 
    # The comprehension iterates over these and accesses the original array at the given index and selets up to the window (row) size
    return [a[i:(i + w)] for i in np.arange(0, stride * s, s)]

b = gen(a, 4, 2)
print(b)
