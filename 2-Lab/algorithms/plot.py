import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pb
from algorithms import method


def plot_and_show(m: method.Method):
    x = np.mgrid[-20:20:150j, -20:20:150j]

    z = 2 * x[0]**2 + 4 * x[1]**2 - 5 * x[0] * x[1] / 2 - 3 * x[1]
    #z = x[0]**2 + x[1]**2

    fig, ax = plt.subplots()
    cp = ax.contour(x[0], x[1], z, levels=50)

    for p in m.segments:
        x = [p[0][0], p[1][0]]
        y = [p[0][1], p[1][1]]
        ax.plot(x, y, color='blue')

    plt.show()

