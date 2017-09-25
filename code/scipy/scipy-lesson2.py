# -*- coding: utf-8 -*-

"""
拟合优化
"""

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


X = np.array([ 8.19, 2.72, 6.39, 8.71, 4.7 , 2.66, 3.78])
Y = np.array([ 7.01, 2.78, 6.47, 6.71, 4.1 , 4.23, 4.05])
def residuals(p):
	k,b = p
	return Y - (k*X + b)
r = optimize.leastsq(residuals,[1,0])
k,b=r[0]
x = np.arange(0,10,1)
y=k*x + b
plt.plot(x,y)
print k,b


plt.plot(X,Y,'o')
plt.show()