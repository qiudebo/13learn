# -*- coding: utf-8 -*-

'''
知识点：

偏导数：点 x轴、y轴 斜率；极值：极大值、极小值。
最小二乘法：目标函数-偏差平方和最小，这种根据偏差平方和为最小的条件来选择常数a、b的方法叫做最小二乘法。
偏差：真实值（实际测量值）与经验公式估算值的差。
均方误差：它的大小在一定程度上反映了用经验公式来近似表达原来函数的关系的近似程度的好坏。
'''

import numpy as np
import pandas as pd
from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np


'''
第十节 最小二乘法
工程问题：根据两个变量的多组实验数据（样本数据）来找出这两个变量的函数关系的近似表达式。
通常把这样得到的函数的近似表达式叫做经验公式。经验公式建立以后，就可以把生产或者实验中所
积累的某些经验提高的理论上加以分析。
'''
# 例1

t = np.arange(0,8)
# 测量者、真实值
y = [27.0,26.8,26.5,26.3,26.1,25.7,25.3,24.8]
y0 = [27.7,26.8,26.5,26.3,26.1,25.7,25.3,24.8] # 存在异常值、离群点  模拟欠拟合 
# 模拟过拟合
# 模拟欠拟合

fig = plt.figure()
ax = plt.subplot()
#ax.scatter(x,y)
ax.plot(t,y,'o',label=u'测量值')

# 建立y与t的经验公式 y=f(t)
# 从图形可以看出，这些点大致接近一条直线(拟合一条直线)，所以可以认为 y=f(t)是线性函数，设f(t)=at+b；
# 求a、b，
# 分析过程：找出一条实验值和函数值(经验值、估计值)偏差都很小的直线,目标函数 偏差的和很小。
# 得出目标函数：这种根据偏差平方和为最小的条件来选择常数a、b的方法叫做最小二乘法。
# 对目标函数求极值
# 对y、t求偏导数，得到a、b，得到线性方程

def residuals(p): # 偏差(残差)
	a,b=p
	return y-(a*t+b)

# 计算偏差的平方和

r = optimize.leastsq(residuals,[1,0]) #偏差平方和最小，参数a,b初始值，可随意指定，随着迭代次数的增加，k、b，
a,b=r[0]
print a,b
print y-(a*t + b)

# 经验值、估计值
y1 = a*t + b
ax.plot(t,y1,label=u'估计值')

# 坐标信息
ax.set_ylim(20,30) # 坐标范围

ax.set_title(u'刀具磨损速度')
ax.set_xlabel('t(h)')
ax.set_ylabel('y(mm)')
ax.grid(True)
ax.legend() # 图例
# 显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.show()















 






