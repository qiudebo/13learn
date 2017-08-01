#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'


import numpy as np
import matplotlib.pyplot as plt

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
labels = (u"1-17岁", u"18-24岁", u"25-30岁", u"31-35岁", u"36-40岁", u"40+岁")
y = [0.07, 0.15, 0.40, 0.18, 0.11, 0.08]
x = np.arange(len(labels))

colors = np.random.rand(len(labels))

#colors = np.random.rand(N)
#area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii
#area = np.pi * (15 * i for i in y1)**2

area = [i*np.pi*1000 for i in y]

fig, ax = plt.subplots()

ax.set_xticks(x)
ax.set_xticklabels(labels)

ax.scatter(x, y, s=area, c=colors, alpha=0.5)
ax.grid(True)

for a, b in zip(x, y):
    ax.text(a, b, b, ha='center', va='center', fontsize=8, color='green')

# 紧凑布局
fig.tight_layout()

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.show()
