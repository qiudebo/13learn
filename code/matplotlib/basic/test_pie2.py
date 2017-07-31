#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'


import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    vals1 = [1, 2, 3, 4]
    vals2 = [2, 3, 4, 5]
    vals3 = [1]
    fig, ax = plt.subplots()
    labels = 'A', 'B', 'C', 'D'
    ax.pie(vals1, radius=1.2, autopct='%1.1f%%', pctdistance=0.9)
    ax.pie(vals2, radius=1, autopct='%1.1f%%', pctdistance=0.75)
    ax.pie(vals3, radius=0.6, colors='w')
    ax.set(aspect="equal", title='Pie plot with `ax.pie`')
    # plt.legend()
    plt.legend(labels, bbox_to_anchor=(1, 1), loc='best', borderaxespad=0.)
    plt.show()