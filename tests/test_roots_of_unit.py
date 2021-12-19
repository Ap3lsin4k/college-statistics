import matplotlib.pyplot as plt
import numpy as np


def test_root_of_unit():
    x = np.linspace(0, 2*np.pi, 10)
    plt.plot(np.cos(x), np.sin(x), color='green')