#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import matplotlib.pyplot as plt
import numpy as np


def table_plot():
    """
    table plot
    """
    # 生成测试数据
    data = np.array([
        [1, 4, 2, 5, 2],
        [2, 1, 1, 3, 6],
        [5, 3, 6, 4, 1]
    ])

    # 设置标题
    plt.title(u"可视化标题")

    # 设置相关参数
    index = np.arange(len(data[0]))
    color_index = ["r", "g", "b"]

    # 声明底部位置
    bottom = np.array([0, 0, 0, 0, 0])

    # 依次画图,并更新底部位置
    for i in range(len(data)):
        plt.bar(index, data[i], width=0.5, color=color_index[i], bottom=bottom, alpha=0.7, label=u"标签 %d" % i)
        bottom += data[i]

    # 设置图例位置
    plt.legend(loc="upper left", shadow=True)
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # 图形显示
    plt.show()
    return
table_plot()