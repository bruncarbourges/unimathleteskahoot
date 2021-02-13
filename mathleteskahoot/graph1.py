import numpy as np

from matplotlib import pyplot
from config import config

x = np.array(range(6))
y = 5 * x

config(x, y)

pyplot.show()
