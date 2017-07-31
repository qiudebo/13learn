#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

    labels = (u'web', u'Android',u'IOS',u'web', u'Android',u'IOS')

    y1 = (9.51, 26.35, 64.14)  # 我的前半生
    y2 = (12.06, 34.21, 53.73)  # 三生三世十里桃花
    N = 3
    x = np.arange(N)

    # 设置分开的距离
    explode = (0, 0.1, 0)

    # 创建子图
    fig, ax = plt.subplots()

    #ax.set_title("pie")

    # 定义颜色
    colors2 = ['lightcoral', 'purple', 'lightgreen']
    colors1 = ['yellowgreen', 'gold', 'lightskyblue']

    ax.pie(y1, autopct='%1.1f%%', radius=1.2, colors=colors1, pctdistance=0.9)
    ax.pie(y2, autopct='%1.2f%%', radius=1, colors=colors2, pctdistance=0.5)
    ax.pie(y1, radius=0.6, colors='w')
    # ax.pie(y1, explode=explode, labels=labels,
    #        autopct='%1.1f%%', shadow=True,  radius=1.2, pctdistance=0.9, labels=labels)
    #
    # ax.pie(y2, explode=explode, labels=labels,
    #        autopct='%1.2f%%', shadow=True,  radius=1, pctdistance=0.5, labels=labels)

    # 图形的对称
    ax.axis('equal')

    # 模块颜色、标签、百分比、标题、角度、圆形半径，以及某一块凸出（explode）进行设置后，最终呈现的图形效果

    # 饼图半径的设置——radius

    #bbox_to_anchor 控制图例布局
    ax.legend(labels,bbox_to_anchor=(1.05, 1), loc='best', borderaxespad=0.)
    #plt.legend()
    plt.show()

