#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import numpy as np
import matplotlib.pyplot as plt


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii

fig, ax = plt.subplots()
ax.scatter(x, y, s=area, c=colors, alpha=0.5)
ax.grid(True)

for a, b in zip(x, y):
    ax.text(a, b + 0.01, '%1.1f%%' % (b * 100), ha='center', va='center', fontsize=8, color='green')


# 紧凑布局
fig.tight_layout()
plt.show()
