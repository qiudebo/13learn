# -*- coding:utf-8 -*-

import numpy as np
from scipy import linalg
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd

'''
相关系数
t检验-显著性检验 tau
最小二乘法 - 微积分极值定理求偏导数
拟合优度 - 判定系数
MSE：均方误差
点估计：利用估计的回归方程
区间估计：置信区间、预测区间


统计描述

'''
a = np.array([0.9,1.1,4.8,3.2,7.8,2.7,1.6,12.5,1.0,
	2.6,0.3,4.0,0.8,3.5,10.2,3.0,0.2,0.4,1.0,6.8,11.6,1.6,1.2,7.2,3.2])
b = np.array([67.3,111.3,173.0,80.8,199.7,16.2,107.4,185.4,96.1,77.8,64.2,132.2,58.6,174.6,263.5,79.3,14.8,73.5,24.7,
139.4,368.2,95.7,109.6,196.2,102.2])

print a.shape,len(a)
print b.shape,len(b)


r, prob= stats.pearsonr(a,b) # 相关系数
print r,prob




