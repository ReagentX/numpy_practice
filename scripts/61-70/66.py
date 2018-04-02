import numpy as np
from datetime import datetime


dt64 = np.datetime64('2018-02-25 22:10:10')
print(type(dt64))
print(dt64)

dt = dt64.astype(datetime)
print(type(dt))
print(dt)
