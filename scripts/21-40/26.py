import numpy as np
import pandas as pd


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
data = np.genfromtxt(url, delimiter=',', dtype=[float, float, float, float, object])

# Take the fourth column `row[4]` from each row, make a Python list, and convert to a NumPy array
col = lambda x: np.array([row[x] for row in data])
print(col(4))

# The right way to do this
data_pd = pd.read_csv(url, names=['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species'])
# Access the proper column using the name `data_pd['species']`
print(np.array(data_pd['species']))
