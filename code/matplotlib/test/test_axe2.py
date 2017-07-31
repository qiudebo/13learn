#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt


x = np.arange(10)

fig = plt.figure()
ax = plt.subplot(111)

for i in xrange(5):
    line, = ax.plot(x, i * x, label='$y = %ix$'%i)

#获取当前坐标轴的位置
box = ax.get_position()
#将坐标轴的位置上移10%

# ax.set_position([box.x0, box.y0 ,
#                  box.width, box.height * 0.9])
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

# 将图例置于当前坐标轴下
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=5)
#去除样例周边的边框
plt.legend(frameon=False)
plt.show()