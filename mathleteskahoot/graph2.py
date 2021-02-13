import numpy as np

from matplotlib import pyplot
from config import config

x = np.array(range(3))
y = -3 * x + 6

config(x, y)

pyplot.show()
