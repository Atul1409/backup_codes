from matplotlib import pyplot as plt

import numpy as np

import math

angle = np.linspace(0, 2 * math.pi, 100)

fig = plt.figure()

axis = fig.add_subplot(1, 1, 1)

axis.set_facecolor((0, 0, 0))

x = 16 * ( np.sin(angle) ** 3 )

y = 13 * np.cos(angle) - 5* np.cos(2*angle) - 2 * np.cos(3*angle) - np.cos(4*angle)

plt.fill_between(x, y, color='#ff0000')

plt.plot(x, y ,color="red")

plt.title('Heart')

plt.savefig('heart.png')

plt.show()
