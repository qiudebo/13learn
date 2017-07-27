#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'


import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    x = np.linspace(0, 2*np.pi, 400)
    y = np.sin(x**2)
    # 共享x轴/y轴
    plt.subplots(2, 2, sharex='col')
    plt.subplots(2, 2, sharey='row')
    plt.subplots(2, 2, sharex='all', sharey='all')
    plt.subplots(2, 2, sharex=True, sharey=True)
    N = 10
    y1 = np.zeros(N)
    print y1
    plt.show()
