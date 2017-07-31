#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':

    labels = (u"1-17岁", u"18-24岁", u"25-30岁", u"31-35岁", u"36-40岁", u"40+岁")
    x = np.arange(len(labels))
    y = [0.07, 0.15, 0.40, 0.18, 0.11, 0.08]

    width = 0.35  # 条形图的宽度
    fig, ax = plt.subplots()
    fig.suptitle(u'我的前半生', fontsize=14, fontweight='bold')

    rects1 = ax.plot(x, y, 'b-',label=u'我的前半生')

    ax.set_xticks(x)
    ax.set_xticklabels(labels)



    #ax.plot([0], [0.07], 'o')
    ax.plot(x, y, 'o')

    for a, b in zip(x, y):
        plt.text(a, b + 0.01, '%1.1f%%' % (b * 100), ha='center', va='bottom', fontsize=8, color='green')
    plt.ylim(0, 0.45)

    # ax.set_yticks(())   # 隐藏y轴
    ax.yaxis.grid(True)  # 水平网格

    ax.legend()


    # 图形填充
    ax.fill(x,y,'b')
    #plt.fill(x,y,'b')



    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    plt.show()
