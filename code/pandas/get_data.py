# -*- coding:utf-8 -*-

"""
数据集 https://vincentarelbundock.github.io/Rdatasets/datasets.html
数据集介绍
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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


df3 = df[['Sepal.Length','Sepal.Width','Petal.Length','Petal.Width','Species']]

# print df3.groupby('Species').sum()
# print df3.groupby('Species').max()
# print df3.groupby('Species').mean()
# print df3.groupby('Species').min()
# print df3.groupby('Species').var()

# 行列转换
df3.stack() # 行转列
df3.unstack() # 列转行

# 透视表
print pd.pivot_table(df3,values='Sepal.Length',index=['Species'],columns=['Petal.Width'])


# 时间序列
rng = pd.date_range('1/9/2017',periods=60,freq='S')
ts = pd.Series(np.random.randint(0,60,len(rng)),index=rng)
ts.resample('5Min').sum()
rng = pd.date_range('3/6/2017 00:00', periods=5, freq='D')
ts = pd.Series(np.random.randn(len(rng)), rng)
ts_utc = ts.tz_localize('UTC')
ts_utc.tz_convert('US/Eastern') #

# 时间范围转换
rng = pd.date_range('1/1/2017', periods=5, freq='M') # 月末
ts = pd.Series(np.random.randn(len(rng)), index=rng)
ps = ts.to_period() # 
ps = ps.to_timestamp()
# 季度 转换 每个季度第一个月的9点
prng = pd.period_range('2016Q1', '2017Q4', freq='Q-NOV')
ts = pd.Series(np.random.randn(len(prng)), prng)
ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9


# 分类数据类型

df = pd.DataFrame({"id":[1,2,3,4,5,6], "raw_grade":['a', 'b', 'b', 'a', 'a', 'e']})
df["grade"] = df["raw_grade"].astype("category")

df["grade"].cat.categories = ["very good", "good", "very bad"]
print df["grade"]
df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
df["grade"]
df.sort_values(by="grade")
df.groupby("grade").size()

# 画图
ts = pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2013',periods=1000))
ts.cumsum() # 累加

ts.plot()
#plt.show()

df = pd.DataFrame(np.random.randn(1000,4),index=ts.index,columns=['A','B','C','D'])
df = df.cumsum()
plt.figure()
df.plot()
plt.legend(loc='best')
plt.show()

# 数据存

#df3.to_csv("foo.csv") # csv
#df3.to_excel('foo.xlsx', sheet_name='Sheet1') # xlsx











