#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    x = np.linspace(0, 20, 50)
    y = np.sin(x+1) + np.cos(x**2)
    bottom = -0.1
    hold = False
    label = "delta"
    markerline, stemlines, baseline = plt.stem(x, y, bottom=bottom,
                                               label=label)
    plt.setp(markerline, color='red', marker='o')
    plt.setp(stemlines, color='blue', linestyle=':')
    plt.setp(baseline, color='grey', linewidth=2, linestyle='-')
    plt.legend()
    plt.show()
