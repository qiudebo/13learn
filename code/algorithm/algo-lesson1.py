# -*- coding:utf-8 -*-

'''
1.算法的定义，术语的来源及演变
2.最大值、线性搜索、排序、二分搜索
排序：冒泡、插入、选择、二分插入、归并、快速
3.贪心算法--最优化问题


算法
大O记法
复杂度

度量算法的计算复杂度使用大O算法

时间、空间复杂度

'''




import numpy as np
import pandas as pd
from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,10)
print x

y = 100*x**2 + 17*x + 4

plt.plot(x,y)
plt.plot(x,x**3)
plt.show()