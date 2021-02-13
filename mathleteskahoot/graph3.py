import numpy as np

from matplotlib import pyplot
from config import config

x = np.array(range(-7, 7, 1))
y = (x + 6) * (x - 1)

config(x, y)

pyplot.show()
