from ipywidgets import interactive
from IPython.display import display
import numpy as np
import matplotlib.pyplot as plt

def gauss(p, w):
    x=np.linspace(0.0, 1.0, 100)
    y=2**(-(x-p)**2/w**2)
    plt.plot(x, y)
    plt.show()

g=interactive(gauss, p=(0.0,1.0), w=(0.1, 0.5))
display(g)
