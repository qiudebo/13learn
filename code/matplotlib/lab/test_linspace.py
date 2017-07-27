#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    # 等差数列
    N = 8
    y = np.zeros(N)
    x1 = np.linspace(0, 10, N, endpoint=True)
    x2 = np.linspace(0, 10, N, endpoint=False)
    plt.plot(x1, y, 'o')
    plt.plot(x2, y + 0.5, 'o')
    plt.ylim([-0.5, 1])
    plt.show()