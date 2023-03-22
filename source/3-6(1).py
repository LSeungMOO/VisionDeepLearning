import numpy as np
import matplotlib.pyplot as plt

def gaussian_1d(x, mu, sigma):
    return np.exp(-((x - mu) / sigma) ** 2 / 2) / (sigma * np.sqrt(2 * np.pi))

# 예시
x = np.linspace(-6, 6, 100)
y = gaussian_1d(x, 0, 1)
plt.plot(x, y)
plt.show()