#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

    fig, ax = plt.subplots()

    ax.plot([1, 2, 3])
    ax.set_title('a simple figure')
    fig.canvas.draw()

    X = np.array(fig.canvas.renderer._renderer)
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111, frameon=False)
    ax2.imshow(X)
    plt.show()