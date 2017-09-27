# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3)
y = np.square(x)

fig = plt.figure()
ax = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)
ax4 = plt.subplot(224)
#plt.sca(ax)
ax.scatter(x,-y)
ax.plot(x,-y)
# plt.sca(ax2)
ax2.plot(x,y)

# 圆的生成算法
a = np.linspace(-2*np.pi,2*np.pi)
radius = 1
x3 = radius*np.cos(a)
y3 = radius*np.sin(a)

ax3.plot(x3,y3)

#椭圆的生成算法
r1 = 2
r2 = 6
x4 = 1 + r1*radius*np.cos(a)
y4 = 5 + r2*radius*np.sin(a)
ax4.set_xlabel('x4') # 坐标轴标签
ax4.set_ylabel('y4')
ax4.set_xlim(-2,6)  # 坐标范围
ax4.set_ylim(-2,12)
ax4.set_title(u'oval') # 标题
ax4.plot(x4,y4,label='oval')
ax4.grid(True) # 网格
ax4.legend() # 图例
#b = [-2,0,2,4,6]
#ax4.set_xticks(b) # 刻度
#ax4.set_xticklabels(['a','b','c','d','e']) # 刻度标签
ax4.fill(x4,y4,'b') # 填充
ax4.fill_between((5,7),(6,7))
plt.show()

# 平移



