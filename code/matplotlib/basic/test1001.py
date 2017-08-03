#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    x = np.linspace(-1,1)

    y = (np.pi*x)**2
    # y = x**2+1

    y = np.sin(x)
    plt.plot(x,y)
    plt.show()