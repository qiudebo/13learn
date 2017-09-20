# -*- coding: utf-8 -*-

## http://www.scipy-lectures.org/intro/numpy/array_object.html#creating-arrays


import numpy as np


## 创建数组
### 方式一：定义数组 （手动输入）
####一维
a = np.array([0,1,2,3])
a.ndim
a.shape
len(a)
#### 多维
b = np.array([[0,1,2],[3,4,5]])
b.ndim
b.shape
len(b)



### 方式二：函数 （使用函数创建数组）

#### 均匀间隔的一组数据 指定终点值，等差数列
a = np.arange(10) # 0 ... n-1
b = np.arange(1,9,2) # start end(exclusive) step 开始值、结束值、步长
#### 均匀间隔的一组数据 指定...
c = np.linspace(0,1,6) # start end num-points 开始值 结束值 数量
d = np.linspace(0,1,5,endpoint=False) # 不包含终点
#### 常用数组
a = np.ones((3,3))  # 单位矩阵
b = np.zeros((2,2)) # 零矩阵
c = np.eye(3) # 
d = np.diag(np.array([1,2,3,4]))

#### 随机数
a = np.random.rand(4) # 生成均匀分布的随机数（变量）
b = np.random.randn(4) # 高斯分布
c = np.random.seed(1234) # 设置随机种子

#### np.empty

### 基本数据类型
#### 自动检测数据类型
a = np.array([1, 2, 3]) # int64 
b = np.array([1.,2.,3.]) # float64

#### （显示）指定数据类型
c = np.array([1,2,3],dtype=float)
c.dtype

#### 默认数据类型为实点型
a = np.ones((3,3))
a.dtype


#### 其他的数据类型
d = np.array([1+2j, 3+4j, 5+6*1j]) # 复数类型
d.dtype
e = np.array([True, False, False, True])# 布尔类型
e.dtype
f = np.array(['Bonjour', 'Hello', 'Hallo',]) # 字符串类型
e.dtype


### 基本的可视化

#### 暂时略

### 索引、切片
#### 同 python
a = np.arange(10)
a[0],a[2],a[9]

a[::-1] # 数组反转

a = np.diag(np.arange(3))
a[1,1] # 行 列
a[2,1]
a[1]
#### 切片
a= np.arange(10) # 切片
a[2:9:3] # [start:end:step]

a[:4] # 不包含最后一个索引

a[1:3] # 切片的三部分值都不是必须的， 默认start=0，end为最后一个下标，步长1
a[::2]
a[3:]

#### 赋值和切片
a = np.arange(10)
a[5:] = 10 # 赋值
b = np.arange(5)
a[5:] = b[::-1] # 反转赋值

#### 矩阵相加   生成5*5矩阵
np.arange(6) + np.arange(0, 51, 10)[:, np.newaxis]

#### python拷贝（浅）  检查是否共享内存
a = np.arange(10)
b = a[::2]
np.may_share_memory(a,b)
b[0] = 12


a = np.arange(10)
c = a[::2].copy()
c[0] = 12
np.may_share_memory(a,c)

#### 素数
is_prime = np.ones((100,), dtype=bool)

is_prime[:2] = 0

N_max = int(np.sqrt(len(is_prime) - 1))
for j in range(2, N_max + 1):
	is_prime[2*j::j] = False

#### 使用布尔码
np.random.seed(3)
a = np.random.random_integers(0, 20, 15)
(a % 3 == 0)
mask = (a % 3 == 0)
extract_from_a = a[mask]
extract_from_a

a[a % 3 == 0] = -1
a

#### 索引整型数据
a = np.arange(0, 100, 10)
a[[2, 3, 2, 4, 2]]
a[[9, 7]] = -100  # 赋值




