import numpy as np
import matplotlib.pyplot as plt
from math import *


x, y = np.mgrid[-3*np.pi:3*np.pi:300j,
                -3*np.pi:3*np.pi:300j]
z = np.sqrt(-x) + np.sqrt(-y)

fig, ax = plt.subplots()

ax.contour(z, levels = 20)

fig.set_figwidth(12)    #  ширина и
fig.set_figheight(12)    #  высота "Figure"

plt.xlim([0, -100])
plt.ylim([0, -100])

plt.show()