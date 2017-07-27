#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import matplotlib.pyplot as plt


if __name__ == '__main__':
    plt.subplot(211)
    plt.plot(range(12))
    plt.subplot(212, facecolor='y')
    plt.show()