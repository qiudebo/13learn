#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':

    # 等比数列
    N = 10
    x1 = np.logspace(0.1, 1, N, endpoint=True)
    x2 = np.logspace(0.1, 1, N, endpoint=False)
    y = np.zeros(N)
    plt.plot(x1, y, 'o')
    plt.plot(x2, y + 0.5, 'o')
    plt.ylim([-0.5, 1])
    plt.show()