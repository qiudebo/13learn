# -*- coding: utf-8 -*-

import numpy as np
from numpy import linalg as LA

# 对角线法则只适合二阶与三阶行列式

# 例1 二阶行列式 求解线性方程 计算系数矩阵的逆 与 常数矩阵的点积
a = np.array([[3,-2],[2,1]])
b = np.array([12,1])
x = np.linalg.inv(a).dot(b)
print x

D = np.linalg.det(a) # 方阵的行列式
D1 = np.array([[12,-2],[1,1]])
D2 = np.array([[3,12],[2,1]])

print D
print np.linalg.det(D1)
print np.linalg.det(D2)

# 矩阵计算
A = np.matrix([[3,-2],[2,1]])
B = np.matrix([[12],[1]])
X = A ** (-1) * B
print X

# 例2  三阶行列式

D = np.array([[1,2,-4],[-2,2,1],[-3,4,-2]])

print np.linalg.det(D)

# n 阶行列式

# 例7
D = np.array([[3,1,-1,2],[-5,1,3,-4],[2,0,1,-1],[1,-5,3,-3]])
print np.linalg.det(D)

# 例8
D = np.array([[3,1,1,1],[1,3,1,1],[1,1,3,1],[1,1,1,3]])
print np.linalg.det(D)

# 例14
D = np.array([[2,1,-5,1],[1,-3,0,-6],[0,2,-1,2],[1,4,-7,6]])

print np.linalg.det(D)

# 例15
D = np.array([[1,1,1,1],[1,2,4,8],[1,3,9,27],[1,4,16,64]])
print np.linalg.det(D)



