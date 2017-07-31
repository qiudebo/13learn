#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import matplotlib.pyplot as plt
from math import pi

if __name__ == '__main__':

    data1 = (8.5, 8.2, 7.7, 7.8, 7.9, 8.4, 8.1, 8.3, 8.1, 8.1, 10.0, 8.5)
    data2 = (8.9, 8.5, 8.2, 8.0, 7.9, 8.3, 8.0, 8.1, 7.9, 8.0, 9.3, 8.9)
    labels = (u"白羊座", u"双鱼座", u"水平座", u"摩羯座", u"射手座", u"天蝎座",
              u"天秤座", u"处女座", u"狮子座", u"巨蟹座", u"双子座", u"金牛座")

    N = len(labels)
    x_as = [n / float(N) * 2 * pi for n in range(N)]

    data1 += data1[:1]
    x_as += x_as[:1]

    data2 += data2[:1]

    plt.rc('axes', linewidth=0.5, edgecolor="#888888")

    ax = plt.subplot(111, polar=True)

    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    ax.set_rlabel_position(0)

    ax.xaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)
    ax.yaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)

    plt.xticks(x_as[:-1], [])

    plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"])

    ax.plot(x_as, data1, linewidth=0, linestyle='solid', zorder=3, label=u'我的前半生')
    ax.plot(x_as, data2, linewidth=0, linestyle='solid', zorder=3, label=u'三生三世十里桃花')

    ax.fill(x_as, data1, 'b', alpha=0.3)
    ax.fill(x_as, data2, 'g', alpha=0.3)

    plt.ylim(0, 10)

    for i in range(N):
        angle_rad = i / float(N) * 2 * pi

        if angle_rad == 0:
            ha, distance_ax = "center", 10
        elif 0 < angle_rad < pi:
            ha, distance_ax = "left", 1
        elif angle_rad == pi:
            ha, distance_ax = "center", 1
        else:
            ha, distance_ax = "right", 1

        ax.text(angle_rad, 10 + distance_ax, labels[i],
                size=10, horizontalalignment=ha, verticalalignment="center")

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # plt.legend()
    plt.show()