# -*- coding:utf-8 -*-

"""
数据集 https://vincentarelbundock.github.io/Rdatasets/datasets.html
数据集介绍
"""

import numpy as np
import pandas as pd

# 读取csv
df = pd.read_csv('./data/iris.csv',encoding='utf-8')
df.columns.name='col' # 定义列的属性名

# 查看数据
df.head(3)  # 前三行
df.tail(3)  # 后三行


df.count(axis=0) # 每列的行数
df.shape # 行数、列数

df.dtypes # 列的数据类型

df.columns # 列索引
df.index   # 行索引
df.values # 元素值

# 数据的汇总统计，基本统计量的描述
df.describe()

# 数据转置、行列转换
df.T

# 排序
df.sort_index(axis=0,ascending=False) # 按照坐标轴排序,即：按照行索引或者列索引 排序

df.sort_values(by='Sepal.Length') # 按列值排序
df.sort('Sepal.Length',ascending=False)

# 数据选择 数据操作   取值

df[0:3]    # 所有列的前三行
df['Sepal.Length'] # 选择指定列
df['Sepal.Length'][0:3] # 选择指定列的前三行


df.loc[1]  # 通过索引选择，第二行
df.loc[0:2] # 前三行

df.loc[0:2,['Sepal.Length','Sepal.Width']] # 指定行索引 和 列索引

df.iloc[0] # 第一行
df.iloc[0:3,0:3] # 选择行列

df.iloc[[1,2,4],[0,2]]  #

df.iloc[1:3,:]  # 前2行所有列

df.iloc[1,1] # 取值

# 布尔索引    数据过滤

df[df['Sepal.Length']>7] # 列值 过滤数据

df1 = df[df>7] # DataFrame过滤数据

# 追加一列

# 追加多行

# 赋值

# 删除行、列

# 缺失值处理
df1.dropna(how='any') # 删除所有存在NaN的行
df1.fillna(df.mean()) # 填充缺失值

pd.isnull(df1) # 判断是否为NaN，返回布尔值


# 统计
df.mean() # 对列求均值，默认 axis=0 列索引 mean()
df.mean(axis=1)

df.loc[0:3]
df.loc[0:3,['Sepal.Length','Sepal.Width','Petal.Length','Petal.Width']].apply(np.cumsum) # apply()

# 合并



# 分组

df2 = df.drop(0,axis=0)
print df2






