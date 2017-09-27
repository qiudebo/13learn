# -*- coding: utf-8 -*-

## http://www.scipy-lectures.org/intro/numpy/array_object.html#creating-arrays


# 推荐使用如下方式导入NumPy函数库
import numpy as np

##  NumPy提供了两种基本对象，ndarray n维数组对象，存储单一数据类型的多维数组，即：数组 ；常用函数
## 高效的存储 大量数组元素，并提供计算的运算速度
## 
## 数组-包含坐标轴  正数、负数
## 
## 



## 创建数组
### 方式一：定义数组 （手动输入）
####一维
a = np.array([0,1,2,3])
a.ndim
a.shape  # 数组的维度,返回元组
a.reshape(2,2) # 创建指定维度的数组
a.dtype # 通过dtype获得元素类型
len(a)

# 从类型字典中获得类型列表
np.typeDict.values(),type(np.typeDict.values()),len(np.typeDict.values())
np.typeDict.keys()

# 单个数值计算 numpy 比python内置类型的运算速度慢很多

# astype() 对数值的元素类型进行转换

t1 = np.array([1,2,3,4],dtype=np.float)
print t1.dtype
t2 = t1.astype(np.float32)
print t2.dtype
#### 多维
b = np.array([[0,1,2],[3,4,5]])

b.ndim
b.shape
len(b)

### 自动生成数值

### 方式二：函数 （使用函数创建数组）

#### 均匀间隔的一组数据 指定终点值，等差数列 类似于内置的range()
a = np.arange(10) # 0 ... n-1
b = np.arange(1,9,2) # start end(exclusive) step 开始值、终值、步长
#### 均匀间隔的一组数据 指定...
c = np.linspace(0,1,6) # start end num-points 开始值 结束值 元素个数 ，创建等差数列的一维数组
d = np.linspace(0,1,5,endpoint=False) # 不包含终点
 
e = np.logspace(0,2,5) # 基数通过base参数指定，默认值为10，开始值0，终值100的5个数，创建等比数列的一维数组

#### 常用数组  创建指定形状的数组

a = np.ones((3,3))  # 单位矩阵 
b = np.zeros((2,2)) # 零矩阵
c = np.eye(3) #  单位阵

d = np.diag(np.array([1,2,3,4])) # 对角阵
#### np.empty() 只分配数组所使用的内存，不对数组元素进行初始化
## zeros()将数组初始化为0，ones()将数组初始化为1

# np.full()  将数组初始化为指定的值
np.full(4,np.pi)

# zeros_like() ones_like() empty_like() full_like() 等函数创建与参数数组的形状和类型相同的数组

np.zeros_like(a)
np.zeros(a.shape,a.dtype)
a.shape,type(a.shape)
# 从字节序列或文件创建数组 frombuffer() fromstring() fromfile()
s="abcdefgh"
ss = np.fromstring(s,dtype=np.int8) # 8位的整数数组

#### 随机数
a = np.random.rand(4) # 生成均匀分布的随机数（变量）
b = np.random.randn(4) # 高斯分布
c = np.random.seed(1234) # 设置随机种子


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
#### 切片，与列表不同，通过切片获得的新数组是原数组的一个视图/快照,它与原数组共享一块数据存储空间

a= np.arange(10) # 切片
a[2:9:3] # [start:end:step]

a[:4] # 不包含最后一个索引

a[1:3] # 切片的三部分值都不是必须的， 默认start=0，end为最后一个下标，步长1
a[::2]
a[3:]

#### 赋值和切片 ,下标存取

a = np.arange(10)
print a
b = a[3:7]
print b
b[2]=100
print b
print a

# 使用整数列表(一维数组)对数组元素进行存取，不和原数组共享内存（数据）
x = np.arange(10,1,-1)
print x
a = x[[3,3,1,8]] 
b = x[[3,3,-3,8]] # 数组-包含坐标轴  正数、负数
b[2] = 100
x[[3,5,1]]=-1,-2,-3
print a
print b
print x

# 下标是一维数组 多维数组

print x[np.array([[1,1,1],[1,1,1]])].reshape(3,2)


# 下标 布尔
x = np.arange(5,0,-1)
print x
print x[np.array([True,False,True,False,False])]

print x[[True,False,True,False,False]]

print x[[True,False,True,True]]

# 产生一个随机整数数组，均匀分布
x = np.random.randint(0,10,6)
print x>5,x[x>5]


# 多维数组  多轴  下标-元组  0轴 1轴
print np.arange(0,60,10)
a = np.arange(0,60,10).reshape(-1,1)
print a
print np.arange(0,6)
print a + np.arange(0,6)

idx = slice(None,None,3)
print idx
print slice(2,None)
print a[idx]

# 切片在[]中使用冒号:隔开的两个或三个整数表示切片
# slice 函数

x = np.array([[0,1],[2,3]])
print x
y = np.array([[-1,-2],[-3,-4]])
print y

