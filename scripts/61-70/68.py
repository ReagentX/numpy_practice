import numpy as np


# `start + (step * stop)` means we make the endpoint whatever the highest value should be
f = lambda start, step, stop: np.arange(start, start + (step * stop), step)
print(f(5, 3, 10))
