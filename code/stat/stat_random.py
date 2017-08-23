# -*- coding: utf-8 -*-

from numpy import array
from numpy.random import normal, randint

data1 = np.array([1, 2, 3])  # 使用ndarray来创建一维数组
data2 = np.random.normal(0, 1, size=100)  # 随机产生一组均值为0、方差为1的正态分布的结果
data3 = np.random.randint(0, 2, size=100)  # 随机产生一组100次抛硬币的结果

print data1
print data2
print data3