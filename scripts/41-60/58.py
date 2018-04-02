import numpy as np


a = np.random.randint(0, 5, 10)
print(a)

# Convert to a list so we can access the count() function
a = list(a)

'''
Use comprehension to solve this more easily than using NumPy
By enumerating the list, we can index the list up to the current item to check for duplicates
This way we fulfill the requirement of making the first occurance False
'''
b = np.array([True if a[:i+1].count(x) > 1 else False for i, x in enumerate(a)])
print(b)
