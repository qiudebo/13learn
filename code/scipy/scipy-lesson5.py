# -*- coding:utf-8 -*-

'''
线性代数
线性方程组

'''

from scipy import linalg
import numpy as np

m,n = 500,50
A = np.random.rand(m,m)
B = np.random.rand(m,n)
X1 = linalg.solve(A,B)
X2 = np.dot(linalg.inv(A),B) # solve 解线性方程 inv 计算逆矩阵 dot计算矩阵的乘积


# 特征值 特征方程

A = np.array([[1,-0.3],[-0.1,0.9]])
print linalg.eig(A)













