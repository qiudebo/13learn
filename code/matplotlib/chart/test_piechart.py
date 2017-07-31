#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import matplotlib.pyplot as plt

if __name__ == '__main__':
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)
    fig1,ax1 = plt.subplots()
    # 设置阴影 弧度
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True,startangle=90)
    # 图形的对称
    ax1.axis('equal')
    plt.savefig("test_piechart.png")
    plt.show()