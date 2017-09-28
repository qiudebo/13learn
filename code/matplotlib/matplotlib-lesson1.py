# *-* coding:utf-8 *-*

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import style
import os
from os import path
from matplotlib.font_manager import fontManager


'''
在平面坐标系中绘制正弦、余弦曲线的步骤：
1.绘制坐标轴
2.设置坐标轴标签
3.设置刻度
4.设置刻度标签
5.设置刻度显示范围
6.绘制曲线
7.显示图例
8.显示网格
9.添加注释
10.添加标题
'''

x = np.arange(0,4*np.pi,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
fig = plt.figure() # 创建figure对象，即：创建画布
ax = plt.subplot(111) # 添加子图
ax.set_xlabel('x') # 设置坐标轴
ax.set_ylabel('y')
ax.set_xticks(np.arange(0,4*np.pi,0.5*np.pi)) # 设置刻度
ax.set_yticks(np.arange(-10,10,0.5))
ax.set_xlim(0,2*np.pi) # 设置刻度范围
ax.set_ylim(-2,2)
ax.plot(x,y1,'b',label='sin x') # 绘制图形
ax.plot(x,y2,'r',label='cos x')
ax.legend(loc='best') # 显示图例
ax.text(0.5*np.pi,1.1,'max') # 添加注释
ax.text(0.5*np.pi,-1.2,'min')
ax.grid() # 显示网格
ax.set_title('y=f(x)') # 设置标题
plt.show() #在屏幕显示Figure对象








