# -*- coding: utf-8 -*-

import numpy as np

# numpy.random 模块提供了大量的随机数相关函数，便于后面用随机数测试各种运算函数

# 产生随机数
print np.random.rand(4,3)
print np.random.randint(0,10,(4,3))
print np.random.uniform(10,20,(4,3))

print np.random.choice(10)
print np.random.randn(2,2)
print np.random.normal(100,10,(4,3))
print np.random.poisson(2.0,(4,3))
print np.random.shuffle(np.random.randint(0,10,10))
print np.random.seed(10)

a = np.array([1, 10, 20, 30, 40])
print np.random.permutation(10)
print np.random.permutation(a)
b = np.random.shuffle(a)
print '-----'
print a

# choice  随机抽取，size：指定输出数组的形状 replace 可重复抽取true，p每个元素抽取的概率

# 放回抽样，不放回抽样
a = np.arange(10,24,dtype=float)
print np.random.choice(a,size=(4,3),replace=False,p=a/np.sum(a))

# 通过seed()函数指定随机数的种子，保证每次运行时重现相同的随机数
np.random.seed(32)
r1 = np.random.randint(0,100,3)
np.random.seed(32)
r2 = np.random.randint(0,100,3)
print r1
print r2

# 求和、平均数、方差

np.random.seed(42)
a = np.random.randint(0,10,size=(4,5))
# 0 轴，1轴
print a
print np.sum(a,axis=0),np.sum(a,axis=1)

print np.ones((2, 3, 4))













