#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'


from matplotlib import pyplot as plt

if __name__ == '__main__':
    # 生成图形
    plt.figure()
    # 添加标题
    plt.title("chart", loc='center')
    # 为 x轴 y轴 添加标签
    plt.xlabel("x")
    plt.ylabel("y")
    # 展示图例
    #plt.legend()

    # 确定坐标系的范围
    plt.xlim(1, 10)
    plt.ylim(1, 10)
    plt.axis()

    # 添加文字说明

    plt.text(2, 2, "test")



    # 显示网格
    plt.grid(True)

    # 添加文本注释（特殊点）
    plt.annotate('hah',xy=(4,4),xytext=(5,5),arrowprops=dict(facecolor='black', shrink=0.05),)


    # 在屏幕显示  plt.show()显示图
    plt.show()
    colors = plt.colors()
    print colors