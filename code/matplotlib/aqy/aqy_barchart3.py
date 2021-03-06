#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'


import matplotlib.pyplot as plt
import numpy as np


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                '%d' % int(height),
                ha='center', va='bottom')

if __name__ == '__main__':

    labels = (u"1-17岁", u"18-24岁", u"25-30岁", u"31-35岁", u"36-40岁", u"40+岁")
    x = np.arange(len(labels))
    print x
    y = [0.07, 0.15, 0.40, 0.18, 0.11, 0.08]
    
    width = 0.35  # 条形图的宽度
    fig, ax = plt.subplots()
    fig.suptitle(u'年龄', fontsize=14, fontweight='bold')


    y1 = [-0.22, -0.18, -0.27, -0.16, -0.12, -0.05]

    rects1 = ax.bar(x, y, width, color='g', label=u'我的前半生')
    rects2 = ax.bar(x, y1, width, color='b', label=u'三生三世十里桃花')

    # ax.set_yticks(())

    ax.set_xticks(x)
    ax.set_xticklabels(labels)


    plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    ## ax.plot([0], [0.07], 'o')


    ## 设置数字标签


    # ha 水平对齐 horizontalalignment
    # va 垂直对齐 verticalalignment
    # fontsize 文字大小

    for a, b in zip(x, y):
        plt.text(a, b+0.01, '%1.1f%%' % (b*100), ha='center', va='bottom', fontsize=8,color='green')

    for a, b in zip(x, y1):
        plt.text(a, b - 0.02, '%1.1f%%' % ((-b) * 100), ha='center', va='bottom', fontsize=8, color='green')

    plt.ylim(-0.45, 0.45)

    #ax.yaxis.grid(True) # 水平网格
    #ax.xaxis.grid(True)

    ax.legend()

    plt.show()


