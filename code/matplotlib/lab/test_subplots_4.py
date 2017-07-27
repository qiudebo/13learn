#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    x = np.linspace(0, 2*np.pi, 400)
    y = np.sin(x**2)

    #fig, axes = plt.subplots(2, 2)

    # polar 极坐标
    fig, axes = plt.subplots(2, 2, subplot_kw=dict(polar=True))
    axes[0, 0].plot(x, y)
    axes[0, 1].scatter(x, y)
    N = 10
    x1 = np.logspace(0.1, 1, 10, base=10, endpoint=True)
    print x1
    plt.show()