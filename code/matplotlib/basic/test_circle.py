#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    pi, sin, cos = np.pi, np.sin, np.cos
    r1 = 1
    r2 = 2

    theta = np.linspace(0, 2*pi, 36)

    x1 = r1 * cos(theta)
    y1 = r1 * sin(theta)

    x2 = r2 * cos(theta)
    y2 = r2 * sin(theta)

    # plt.scatter(x1, y1)
    # plt.scatter(x2, y2)
    plt.plot(x1, y1)

    plt.plot(x2, y2)

    plt.fill(x2,y2,'r')
    plt.fill(x1, y1,'b')

    plt.savefig("circle.png")
    plt.show()