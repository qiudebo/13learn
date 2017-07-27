#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    plt.figure()
    plt.grid(True)

    data = np.linspace(1, 10, 50)
    plt.plot(data)



    plt.show()
