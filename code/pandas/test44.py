# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

#DataFrame 二维数组


df2 = pd.DataFrame({'foo': ['one','one','one','two','two','two'],
                               'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                               'baz': [1, 2, 3, 4, 5, 6]})

df3 = pd.DataFrame([['a', 1], ['a', 2], ['b', 1], ['b', 2]],
                           columns=['A', 'B'])

print df3
print df3.groupby('A').sum()
print df3.groupby('A').mean()
print df3.groupby('A').var()
print df3.groupby('A').max()
print df3.groupby('A').min()
print df3
#print df3.reindex(['C','D'])



df5 = pd.DataFrame({'foo': ['one','one','one','two','two','two'],
                               'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                               'bab':['M','N','O','M','N','N'],
                               'baz': [1, 2, 3, 4, 5, 6],
                               'bax': [11,22,33,44,55,66]
                               })
df6 = pd.DataFrame({'foo': ['one','one','one','two','two','two'],
                               'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                               'bab':['M','N','O','M','N','N'],
                               'baz': [1, 2, 3, 4, 5, 6],
                               'bax': [11,22,33,44,55,66],
                               'baw':[7,8,9,10,11,12]
                               })

df7 = pd.DataFrame({'foo': ['one','one','one','two','two','two'],
                               'bau': [1,2,3,4,5,6]
                               })

df8 = pd.DataFrame({'foo': ['one','one','one','two','two','two'],
	                           'bar': ['A','B','E','F','G','H'],
                               'bau': [1,2,3,4,5,6],
                               'baz': [1, 5, 3, 4, 5, 6]
                               })

# 分组求和
print df5
#print df5.groupby(['bab','bar']).sum()

print len(df5) # 行


# 合并 
# 关联

#print df5 + df5
#print df5.merge(df6) # 合并
#print df5.merge(df7) # 

#print pd.merge(df5,df8,on=['foo','bar'])
# 堆叠
frames = [df5,df7,df8]
df9 = pd.concat(frames)




#print df5.unstack(level=2) # 行转列
#print df5.stack(level=-1) # 列转行


# print df5.pivot(index='foo',columns='bar',values='baz')
# print df5.pivot(index='foo',columns='bar',values='baz').mean(axis=0)
# print df5.pivot('foo','bar','baz') # 行索引、列索引、元素值

#print df5.filter(items=['foo','baz']) # 按列名选择
#print df5.filter(regex='^b',axis=1) # 正则
#print df5.filter(like='oo',axis=1)   # 模糊匹配

# 缺失值的处理

# print df5.fillna(1)  # 指定一个值替换缺失值

# print df5.isnull()
# print df5[df5.isnull()] # 判断元素是否为NaN
# print df5.notnull()      
# print df5[df5.notnull()]

# print df5.count() # 返回每行或每列的非NaN元素的个数

# print df5.dropna() # 删除包含NaN的行或列

# 统计函数



# 排序
df10 = pd.DataFrame({'aoo': ['one','one','one','two','two','two'],
                               'ber': ['A', 'B', 'C', 'A', 'B', 'C'],
                               'bab':['M','N','O','M','N','N'],
                               'daz': [3, 2, 3, 4, 1, 6],
                               'cax': [11,22,33,44,55,66]
                               })
print df10
# print df10.sort_index(axis=1)
print df10.sort(columns='daz') 

print df10.set_index(['a','b','c','d','e'])


