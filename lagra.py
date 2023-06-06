import numpy as np
from  scipy.interpolate import lagrange
x = np.array([0, 1.5, 2])
y = np.array([0, 0.682, 0.841])
result = lagrange(x, y)
print(result)