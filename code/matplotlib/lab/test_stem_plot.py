#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import matplotlib.pyplot as plt
import numpy as np

#x = np.linspace(0.1, 2*np.pi, 10)
x = (89, 79, 57, 46, 1, 24, 71, 5, 6, 9, 10, 15, 16, 19, 22, 31, 40, 41, 52, 55, 60, 61, 65, 69, 70, 75, 85, 91, 92, 94)
markerline, stemlines, baseline = plt.stem(x, np.cos(x), '-.')

plt.setp(baseline, 'color', 'r', 'linewidth', 2)

plt.show()