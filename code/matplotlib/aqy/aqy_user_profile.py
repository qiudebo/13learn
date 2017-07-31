#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    fig, ax = plt.subplots(2, 2)

    fig.suptitle(u'用户画像', fontsize=14, fontweight='bold')

    labels = (u"1-17岁", u"18-24岁", u"25-30岁", u"31-35岁", u"36-40岁", u"40+岁")
    x = np.arange(len(labels))
    y = [0.07, 0.15, 0.40, 0.18, 0.11, 0.08]
    width = 0.35  # 条形图的宽度

    y1 = [0.22, 0.18, 0.27, 0.16, 0.12, 0.05]

    ax[0, 0].bar(x, y, width, color='g', label=u'我的前半生')
    ax[0, 0].bar(x + width, y1, width, color='b', label=u'三生三世十里桃花')

    ax[0, 0].set_yticks(())
    ax[0, 0].set_xticks(x + width / 2)
    ax[0, 0].set_xticklabels(labels)

    for a, b in zip(x, y):
        ax[0, 0].text(a, b + 0.01, '%1.1f%%' % (b * 100), ha='center', va='bottom', fontsize=8, color='green')

    for a, b in zip(x, y1):
        ax[0, 0].text(a + width, b + 0.01, '%1.1f%%' % (b * 100), ha='center', va='bottom', fontsize=8, color='green')

    # ax.yaxis.grid(True) # 水平网格
    ax[0, 0].xaxis.grid(True)

    ax[0, 0].legend()

    #### b

    labelsb = (u"硕士以上", u"本科", u"大专", u"高中-中专", u"初中", u"小学")
    xb = (0.13, 0.22, 0.25, 0.18, 0.13, 0.10)
    xb1 = (0.11, 0.19, 0.23, 0.20, 0.17, 0.10)

    widthb = 0.35  # 条形图的宽度

    yb = np.arange(len(labels))

    ax[0,1].barh(yb, xb, widthb, align='center', color='g', label=u'我的前半生')
    ax[0,1].barh(yb + widthb + 0.05, xb1, widthb, align='center', color='b', label=u'三生三世十里桃花')

    ax[0,1].set_yticks(yb + width / 2)
    ax[0,1].set_yticklabels(labelsb)

    ax[0,1].invert_yaxis()
    ax[0,1].set_xlabel('')
    ax[0,1].set_title('')

    # ax.yaxis.grid(True) # 水平网格
    ax[0,1].xaxis.grid(True)


    #### c




    #plt.ylim(0, 0.45)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号



    plt.show()
