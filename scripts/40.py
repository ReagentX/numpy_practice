import numpy as np


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# Ignore the text column since it is pesky
data = np.genfromtxt(url, delimiter=',', dtype='float', usecols=(0, 1, 2, 3))

# Bin a column to specific values, creates a variable as to which bin we are in
bins = np.digitize(data[..., 2], [3, 5, np.inf])
bins_text = ['small', 'medium', 'large']

# Use list compression to generate the list of bins, reshape so that it is vertical, then append to the data array
new_col = np.array([bins_text[bin] for bin in bins]).reshape(len(bins),1)
data = np.append(data, new_col, axis=1)

print(data[::25])
