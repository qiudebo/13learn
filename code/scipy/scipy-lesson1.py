# -*- coding: utf-8 -*-

"""
函数增长速度
数组广播运算
"""

import numpy as np
import scipy.optimize as optimize
import matplotlib.pyplot as plt

def func(x,p):
	A,k,theta = p
	return A*np.sin(2*np.pi*k*x+theta)

def residuals(p,y,x):
	return y-func(x,p)

x = np.linspace(0,2*np.pi,100)
A,k,theta = 10,0.34,np.pi/6
y0 = func(x,[A,k,theta])
np.random.seed(0)
y1 = y0 + 2*np.random.randn(len(x))
p0=[7,0.40,0]
plsq = optimize.leastsq(residuals,p0,args=(y1,x))
print [A,k,theta]
print plsq[0]
plt.plot(x,y1,'o',label="noise")
plt.plot(x,y0,label="real")
plt.plot(x, func(x, plsq[0]),label="fit")
plt.legend(loc="best")
plt.show()

