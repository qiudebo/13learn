# -*- coding: utf-8 -*-

import numpy as np
import scipy.stats as stats

data1 = np.array([1, 2, 3])  # 使用ndarray来创建一维数组
data2 = np.random.normal(0, 1, size=100)  # 随机产生一组均值为0、方差为1的正态分布的结果
data3 = np.random.randint(0, 2, size=100)  # 随机产生一组100次抛硬币的结果
data = np.random.randint(0, 100, size=100) # 从区间[0,100)随机生成100个数

np.mean(data)   # 均值
np.median(data)  # 中位数
stats.mode(data)  # 众数

np.ptp(a)  # 极差
np.var(a)  # 方差
np.std(a)  # 标准差
np.std(a)/np.mean(a)  # 离散系数
