import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def gaussian_2d(x, y, mu_x, mu_y, sigma_x, sigma_y):
    return np.exp(-((x - mu_x) ** 2 / (2 * sigma_x ** 2) + (y - mu_y) ** 2 / (2 * sigma_y ** 2))) / (2 * np.pi * sigma_x * sigma_y)

# 예시
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x, y = np.meshgrid(np.linspace(-6, 6, 100), np.linspace(-6, 6, 100))
z = gaussian_2d(x, y, 0, 0, 1, 1)

ax.plot_surface(x, y, z)

plt.show()