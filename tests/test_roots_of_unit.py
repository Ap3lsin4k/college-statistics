from time import sleep

import matplotlib.pyplot as plt
import numpy as np


def test_root_of_unit():
    for i in range(30):
        x = np.linspace(0, 2*np.pi, i)
        plt.plot(np.cos(x), np.sin(x), color='green')
        plt.show()
        sleep(1)