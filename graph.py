import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 101)
y = np.exp(-x**2 / 2) / np.sqrt(2 * np.pi)

plt.plot(x, y)
plt.show()
