import numpy as np


dates = np.arange(np.datetime64('2018-02-01'), np.datetime64('2018-02-25'), 2)
print(dates)

dates_cont = np.arange(dates[0], dates[-1])
print(dates_cont)
