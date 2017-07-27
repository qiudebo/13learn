#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import matplotlib.pyplot as plt


if __name__ == '__main__':

    # 坐标轴
    # plt.figure()
    # plt.axis([0.1, 0.15, 0.8, 0.75]) #  [xmin, xmax, ymin, ymax]

    plt.axes([0.1, 0.15, 0.8, 0.75]) #  [left, bottom, width,height]
    plt.plot(range(10))
    plt.title(r'$\ddot{o}\acute{e}\grave{e}\hat{O}\breve{i}\bar{A}\tilde{n}\vec{q}$', fontsize=20)
    # shorthand is also supported and curly's are optional
    plt.xlabel(r"""$\"o\ddot o \'e\`e\~n\.x\^y$""", fontsize=20)
    plt.show()

