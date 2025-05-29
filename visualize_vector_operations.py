import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([2, 3])
v2 = np.array([1, 1])
result = v1 + v2

plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r')
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='b')
plt.quiver(0, 0, result[0], result[1], angles='xy', scale_units='xy', scale=1, color='g')

plt.xlim(0, 5)
plt.ylim(0, 5)
plt.grid()
plt.gca().set_aspect('equal')
plt.show()

