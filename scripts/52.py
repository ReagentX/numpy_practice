import numpy as np


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
data = np.genfromtxt(url, delimiter=',', dtype='str', usecols=4)
np.random.seed(100)
d_s = np.sort(np.random.choice(data, size=20))

r = []
c = 0
for i, v in enumerate(d_s, 0):
    # Append the counter variable
    r.append(c)
    # Debug
    print(f'{c}\t{i}: {d_s[i]}, {max(i-1, 0)}: {d_s[max(i-1, 0)]}, {d_s[i] == d_s[max(i-1, 0)]}')
    # If the current item is the same as the next one, add 1, else reset to 0
    if d_s[i] == d_s[min(i+1, len(d_s)-1)]:
        c += 1 
    else:
        c = 0

print(r)
