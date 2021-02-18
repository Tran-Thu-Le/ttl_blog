
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0, 1, 100)
noise=0.05*np.random.normal(size=100)
position = 0.5
halfwidth = 0.1
y=2**(-(x-position)**2/halfwidth**2)+noise
plt.plot(x, y)
plt.fill_between(x, y, facecolor='g', alpha=0.8)
plt.title("Gaussian-type function with noise")
plt.show()
