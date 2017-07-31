#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    plt.rcdefaults()
    fig, ax = plt.subplots()

    labels = (u"硕士以上", u"本科", u"大专", u"高中-中专", u"初中", u"小学")
    x = (0.13, 0.22, 0.25, 0.18, 0.13, 0.10)
    x1 = (-0.11, -0.19, -0.23, -0.20, -0.17, -0.10)

    width = 0.35  # 条形图的宽度

    y = np.arange(len(labels))

    ax.barh(y, x, width, align='center', color='g', label=u'我的前半生')
    ax.barh(y, x1, width, align='center', color='b', label=u'三生三世十里桃花')

    ax.set_yticks(y + width/2)
    ax.set_yticklabels(labels)

    ax.invert_yaxis()
    ax.set_xlabel('')
    ax.set_title('')

    # ax.yaxis.grid(True) # 水平网格
    ax.xaxis.grid(True)

    plt.xlim(-0.3, 0.3)

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    #ax.set_xticks(())  # 隐藏y轴


    # 设置图例

    # plt.legend(loc="lower right", bbox_to_anchor=[1, 0.95],shadow=True,
    #            ncol=1, title="Legend", fancybox=True)

    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
              fancybox=True, shadow=True, ncol=6)

    # 去除样例周边的边框
    # plt.legend(frameon=False)

    ax.get_legend().get_title().set_color("red")

    plt.show()