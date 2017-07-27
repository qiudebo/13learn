#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'


import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    x = np.linspace(0, 2*np.pi, 400)
    y = np.sin(x**3)

    #x2 = np.linspace(0, 2*np.pi, 400)
    #y2 = np.sin(x**2)

    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
    ax1.plot(x, y)
    ax1.set_title('Sharing Y axis')

    # 散点图
    ax2.scatter(x, y)
    plt.show()