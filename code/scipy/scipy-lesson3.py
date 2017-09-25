# -*- coding: utf-8 -*-

"""
函数增长速度
数组广播运算
"""

import numpy as np
import scipy.optimize as optimize
import matplotlib.pyplot as plt


'''
泰勒公式：用n次多项式近似表达函数f(x)
精度要求高、需要估计误差->高次多项式来近似表达函数，给出误差公式
直接使用plt画图，有些属性不支持，如刻度标签。


'''

x = np.linspace(0,2*np.pi,100)
y = np.sin(x)
x1 = [0,np.pi/2,3*np.pi/2,2*np.pi]
y1 = [0,1,-1,0]
t = ['A','C','D','B']
plt.plot(x1,y1,'o')
plt.plot(x,y)

for x1,y1,t1 in zip(x1,y1,t):
	plt.text(x1,y1,t1)

plt.plot([0,2*np.pi],[0,0])

plt.plot([np.pi/3,2*np.pi/3],[1,1],[4*np.pi/3,5*np.pi/3],[-1,-1])


plt.plot([np.pi/2,np.pi/2],[0,1],'--')
plt.plot([3*np.pi/2,3*np.pi/2],[0,-1],'--')


plt.xticks(np.arange(0,2*np.pi,0.5*np.pi))
#plt.([0,'0.5pi','pi','1.5pi','2pi'])

print np.arange(0,5*np.pi/2,0.5*np.pi)
plt.show()



















