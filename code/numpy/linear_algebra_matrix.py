# -*- coding: utf-8 -*-

import numpy as np
from  numpy import linalg as LA

# 实矩阵
A = np.matrix([[1,2,3],
	          [4,5,6]])
print A
# 复矩阵
B = np.matrix([[1,2,3],
	           [4,5,6]],dtype=complex)
print B

# 方阵
A = np.arange(9).reshape((3,3))
print A

# 行矩阵、行向量
A = np.matrix([[1,2,3]])
print A

# 列矩阵、列向量
B = np.matrix([[1],
	           [2],
	           [3]])
print B

#同型矩阵 两个矩阵行数相等、列数也相等
A = np.arange(9).reshape((3,3))
B = np.arange(10,19,1).reshape((3,3))
print A.shape,B.shape

# 零矩阵
O = np.zeros((2,2))
print O

# 单位阵,主对角线为1，其他为0
E = np.eye(3)
print E
# 对角阵
A = np.eye(3)
B = A*2
print B

# 2.2 例4  矩阵相乘，前提条件

A = np.matrix([[1,0,3,-1],
	          [2,1,0,2]])

B = np.matrix([[4,1,0],
	          [-1,1,3],
	          [2,0,1],
	          [1,3,4]])

C = A*B
print C

# 2.2 例5 矩阵相乘不满足交换律,反正法

A = np.matrix([[-2,4],
	           [1,-2]])
B = np.matrix([[2,4],
	           [-3,-6]])

C1 = A*B
C2 = B*A
print C1
print C2

# 矩阵的幂，只适用n阶方阵

A = np.arange(9).reshape((3,3))
print A
E = np.eye(3)
print A*E
print E*A

C1 = A*A # A 不是矩阵，是数组，所以A*A对应元素的乘积，相当于每个元素的平方，如果 矩阵相乘需要dot
C2 = A.dot(A)
C = LA.matrix_power(A,2)
print C1
print C2
print C
print A.dot(A)

# 矩阵线性变换
A = np.matrix([[0,1,1,1],
	           [1,0,0,0],
	           [0,1,0,0],
	           [1,0,1,0]])
print A*A
C = LA.matrix_power(A,2)
print C

# 矩阵的转置
A = np.matrix([[1,2,0],[3,-1,1]])
B = A.T
print A
print B
# 2.2 例7

A = np.matrix([[2,0,-1],[1,3,2]])
B = np.matrix([[1,7,-1],[4,2,3],[2,0,1]])

C = A*B
print C.T
A1 = A.T
B1 = B.T
C1 = B1*A1
print C1

# 对称矩阵 对称阵 ,它的元素以对角线为对称轴对应相等
A = np.ones((2,2))
print A
print A.T

# 方阵的行列式

# 逆矩阵 ，可逆AB=BA=E,行列式不等于0,可逆矩阵是非奇异矩阵

# 2.2 例11 方阵的行列式  方阵的逆
A = np.matrix([[1,2,3],[2,2,1],[3,4,3]])
print LA.det(A)
print LA.inv(A)

# 2.2 例12

A = np.matrix([[1,2,3],[2,2,1],[3,4,3]])
B = np.matrix([[2,1],[5,3]])
C = np.matrix([[1,3],[2,0],[3,1]])

print LA.inv(A)*C*LA.inv(B)

# 2.2 例13
P = np.matrix([[1,2],[1,4]])
L = np.matrix([[1,0],[0,2]])


# 4.1 例4 矩阵的秩

A = np.matrix([[1,2,3],[2,3,-5],[4,7,1]])
print LA.matrix_rank(A)

B = np.matrix([[2,-1,0,3,-2],[0,3,1,-2,5],[0,0,0,4,-3],[0,0,0,0,0]])
print LA.matrix_rank(B)

# 4.1 例5 矩阵的秩
A = np.matrix([[3,2,0,5,0],[3,-2,3,6,-1],[2,0,1,5,-3],[1,6,-4,-1,4]])
print LA.matrix_rank(A)
# 4.1 例6 矩阵的秩
A = np.matrix([[1,-2,2,-1],[2,-4,8,0],[-2,4,-2,3],[3,-6,0,-6]])
print LA.matrix_rank(A)



# 正交阵
# 5.1 例5 特征值、特征向量

# 内积
# 范数，n维向量x的长度


A = np.array([[3,-1],[-1,3]])
print LA.linalg.eigvals(A)
w,v = LA.linalg.eigh(A)
print w,v


# 5.1 例6 
A = np.array([[-1,1,0],[-4,3,0],[1,0,2]])
w,v = LA.linalg.eigh(A)
print w
print v

# 5.1 例7
A = np.array([[-2,1,1],[0,2,0],[-4,1,3]])
w,v = LA.linalg.eigh(A)
print w,v




#







