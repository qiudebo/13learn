#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import matplotlib.pyplot as plt


if __name__ == '__main__':

    # 在坐标系 画一长方形状
    left, width = .25, .5
    bottom, height = .25, .5
    right = left + width
    top = bottom + height
    # polar 极坐标
    ax = plt.gca()
    # rotation 旋转角度
    p = plt.Rectangle((left, bottom), width, height, Fill=False)

    p.set_transform(ax.transAxes)

    p.set_clip_on(False)
    ax.add_patch(p)
    # horizontal alignment 水平对齐
    # vertical alignment 垂直对齐


    # 左上角
    ax.text(left, bottom, 'left top',
            horizontalalignment='left',
            verticalalignment='top',
            transform=ax.transAxes)
    # 左下角
    ax.text(left, bottom, 'left bottom',
            horizontalalignment='left',
            verticalalignment='bottom',
            transform=ax.transAxes)


    plt.show()
