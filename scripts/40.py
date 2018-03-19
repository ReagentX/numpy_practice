import numpy as np
import pandas as pd


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# Ignore the text column since it is pesky
data = np.genfromtxt(url, delimiter=',', dtype='float', usecols=(0, 1, 2, 3))

# Bin a column to specific values, creates a variable as to which bin we are in
bins = np.digitize(data[..., 2], [3, 5, np.inf])
bins_text = ['small', 'medium', 'large']

# Use list compression to generate the list of bins, reshape so that it is vertical, then append to the data array
new_col = np.array([bins_text[bin] for bin in bins])[:, np.newaxis]
data = np.hstack([data, new_col])

print(data[::25])

# The right way to do this
data_pd = pd.read_csv(url, names=['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species'])
labels = ['small', 'medium', 'large']

'''
`pd.cut` slices the column `data_pd['petallength']` to a group based on the array
Labels come from whichever bin the data fall into
`right = false` means the bins do not include the rightmost edge, i.e. for [0, 3] it go up to 3 but does not include it
'''

data_pd['group'] = pd.cut(data_pd['petallength'], [0, 3, 5, np.inf], right=False, labels=labels)
print(data_pd[::25])
