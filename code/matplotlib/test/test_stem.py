#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import numpy as np;
import math;
from matplotlib import *;
import matplotlib.pyplot as plt

x = np.arange(1, 10, 1);
y = np.sin(x);

plt.subplot(321);
plt.scatter(x, y, marker='*');  # 散点图
plt.grid(True);

plt.subplot(322);
plt.plot(x, y);  # 线形连线图

plt.subplot(323);
plt.pie(y);  # 单调的饼状图

plt.subplot(324);
plt.bar(x, y);  # 条状图

plt.subplot(325);
plt.stem(x, y);  # 茎叶图

plt.show();

# 另起一图
fig = plt.figure();
ax = fig.add_subplot(1, 1, 1);
z = np.zeros(9)  # 偏移位置
label = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'I']  # 标签
ax.pie(x, explode=z, labels=label);  # 稍完整些的饼状图
plt.title(u'饼状图')  # 图标题

plt.show();