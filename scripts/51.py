import numpy as np
import pandas as pd


# Generate the random array between two values and display it
a = np.random.randint(1, 5, size=6)
print(a)

# Find the unique values
u = np.unique(a)
# Generate one-hot encodings for the unique values
one_hot = np.eye(len(u))

# Encode by iterating through the original array and pulling the respective one_hot using the index `np.where(u == x)`
encoded = np.array([one_hot[np.where(u == x)][0] for x in a])
print('NumPy:')
print(encoded)

# Pandas example
s = pd.get_dummies(a)
print('Pandas:')
print(s)
