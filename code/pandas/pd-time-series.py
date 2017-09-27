# -*- coding:utf-8 -*-

'''
http://pandas.pydata.org/pandas-docs/stable/10min.html
http://pandas.pydata.org/pandas-docs/stable/timeseries.html#timeseries
'''

import pandas as pd
import numpy as np
from datetime import datetime


rng0 = pd.date_range('1/1/2017',periods=72,freq='H') #周期、频率
rng1 = pd.date_range('1/1/2017',periods=10,freq='D')
rng2 = pd.date_range('1/1/2017',periods=10,freq='M')

ts = pd.Series(np.random.randn(len(rng0)),index=rng0)

converted = ts.asfreq('45Min',method='pad') # 改变频率
ts.resample('D').mean()

start = datetime(2017,9,1)
end = datetime(2017,9,20)

rng = pd.date_range(start,end)

# bdate_range 工作日

# 开始、结束、频率
rng = pd.date_range(start,end,freq='W') # 周日
rng = pd.date_range(start,end,freq='B') # 工作日
rng = pd.date_range(start,end,freq='BM') # 月末的最后一天
rng = pd.date_range(start=start,periods=10)
rng = pd.date_range(start,periods=10,freq='2h20min')
print rng




































