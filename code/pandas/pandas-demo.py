# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Numpy 提供了十分方便的数组处理功能，但缺少数据处理和分析的功能。
# Pandas 基于Numpy开发，提供更多的数据处理和分析的功能。
# Seires 和 DataFrame 是 Pandas 中最常用的两个数据对象。介绍这两个数据对象的基本概念和常用属性。
# 数据对象 Series，由index和values组成，下标存取：使用位置、索引标签

# DataFrame 对象
s = pd.Series([1,2,3,4,5],index=["a","b","c","d","e"])
print u"索引：", s.index
print u"值数组：", s.values

print u"位置下标：", s[2]
print u"标签下标：", s['b']

# 位置切片、标签切片，切片规则：位置不包含结束位置，标签切片包含结束位置
print s[1:3]
print s['b':'d']

# 存取元素，位置列表 位置数据，标签列表 标签数组
print s[[1,3,2]]
print s[['b','d','c']]
# 具有数组和字典的功能
print s.iteritems()
print list(s.iteritems())

# 运算，按照标签对齐
s2 = pd.Series([20,30,40,50,60],index=["b","c","d","e","f"])
print s + s2

# 2 DataFrame  提供多种数据结构转换为DataFrame对象的方法，输入输出函数将数据文件转换为DataFrame队形的方法。
# 数据集 https://vincentarelbundock.github.io/Rdatasets/datasets.html

# 列的数据类型必须一致，不同列可以有不同的数据类型
df_soil = pd.read_csv("data/Soils.csv", index_col=[0, 1])
print df_soil.dtypes
df_soil.columns.name = "Measures"
print df_soil.shape # 行列

# 数据存取 
# 列索引，索引标签
print df_soil.columns
print df_soil.columns.name
# 行索引
print df_soil.index

# DataFrame 有两个轴
# 通过列标签获取指定列
print df_soil["pH"]  # 得到Series对象
print df_soil[["pH","Mg"]] # 得到一个新的DataFrame

# .loc[] 行索引标签获取指定的行
# print df_soil.loc["0-10","Top"]

print df_soil.values.dtype

# DataFrame 对象
df1 = pd.DataFrame(np.random.randint(0,10,(4,2)),index=["A","B","C","D"],columns=["a","b"])
print df1

df2 = pd.DataFrame({"a":[1,2,3,4],"b":[5,6,7,8]},index=["A","B","C","D"])
print df2


arr = np.array([("iteml", 1),("item2",2),("item3",3),("item4",4)],
	dtype=[("name", "10S"), ("count", int)])

print arr.shape,type(arr)
df3 = pd.DataFrame(arr)
print df3
# 列表字典 嵌套字典 转换为DataFrame对象  
dict1 = {"a":[1,2,3],"b":[4,5,6]}
dict2 = {"a":{"A":1,"B":2},"b":{"A":3,"C":4}}
print dict2

df1 = pd.DataFrame.from_dict(dict1,orient="index")
print df1
df2 = pd.DataFrame.from_dict(dict1,orient="columns")
print df2
# 缺失值 NaN
df3 = pd.DataFrame.from_dict(dict2,orient="index")
print df3
df4 = pd.DataFrame.from_dict(dict2,orient="columns")
print df4

items = dict1.items()
print items,type(items)

df1 = pd.DataFrame.from_items(items,orient="index",columns=["A","B","C"])
df2 = pd.DataFrame.from_items(items,orient="columns")
print df1
print df2

# to_dict() 将 DataFrame 转换为dict

print df2.to_dict(orient="records")
print df2.to_dict(orient="list")
print df2.to_dict(orient="dict")

# to_records() 将DataFrame对象转换为结构数组
print df2.to_records().dtype
print df2.to_records(index=False).dtype

# index 对象  索引标签
index = df_soil.columns
print index
print index.values
# 新的index对象
print index[[1,3]]
print index[1::2]
print index[index>'c']

#get_loc
print index.get_loc('Ca')
print index.get_indexer(['Dens', 'Conduct', 'nothing'])
# Index
index = pd.Index(["A","B","C","D","E"],name="level")
s1 = pd.Series([1,2,3,4,5],index=index)
df1 = pd.DataFrame({"a":[1,2,3,4,5],"b":[6,7,8,9,10]},index=index)
print df1
print s1
print index

# MultiIndex

# function

print df_soil.mean()
print df_soil.mean(axis=1)

print df_soil.head()
print df_soil.tail()

np.random.seed(42)
df = pd.DataFrame(np.random.randint(0,10,(5,3)),
	index=["r1","r2","r3","r4","r5"],
	columns=["c1","c2","c3"])
print df
print df[2:4]
print df["r2":"r4"]
print df.c1>4
print df[df.c1>4]

print df[df>2]

dfNaN = df[df>2]

print df_soil[(df_soil.pH>5)&(df_soil.Ca<11)]
# query()
print df_soil.query("pH>5 and Ca<11").head(2)
# 在表达式中使用全局变量或局部变量的值
pH_low = 5
Ca_li = 11

print df_soil.query("pH>@pH_low and Ca<@Ca_li")

print df_soil['pH'].count()

# where

# append

# 序列化 to_pickle() read_pickle()

df_soil.to_pickle("soil.pickle")
df_soil2 = pd.read_pickle("soil.pickle")
print df_soil2
print df_soil2.equals(df_soil)

# 数值运算符 参数 axis：指定运算对应的轴 level：索引级别 skipna：是否略过NaN
# dfNaN
# add() sub() mul() div() mod()
# fill_value
print dfNaN

t = np.linspace(0,10,400)
x = np.sin(0.5*2*np.pi*t)
s = pd.Series(x,index=t)
# 相邻的N个元素进行移动窗口运算
s_mean = pd.rolling_mean(s,5,center=True) # 计算移动平均
print s_mean

# 字符串
s_abc = pd.Series(["a","b","c"])
print s_abc.str.upper()

# str.decode() 转换为Unicode字符串的序列
# str.encode() 把Unicode字符串按照指定的编码转换为字节字符串

s_utf8 = pd.Series([b"北京",b"朝阳",b"立水桥"])
print s_utf8
s_unicode = s_utf8.str.decode("utf-8")
print s_unicode
s_gb2312 = s_unicode.str.encode("gb2312")
print s_gb2312

# 无序分类 、有序分类

print df_soil.Depth

# 时间序列，时间点、时间段、时间间隔

# 判断元素是否为NaN
print dfNaN.isnull()
print dfNaN.notnull()
print dfNaN
print dfNaN.count()
print dfNaN.count(axis=1)

#soils = df_soil[["Contour","Depth","pH","N","Dens","P","Ca","Mg","K","Na","Conduc"]]
soils = df_soil[["Contour","Depth","pH","N","Dens","P"]]
soils_mean = soils.groupby(["Depth","Contour"]).mean()
print soils_mean

# 添加删除 行列


# 行索引和列  将行索引转换为列

print soils_mean.reset_index(level="Contour").head()

# 将列转换为行索引 set_index()

# 透视表

















