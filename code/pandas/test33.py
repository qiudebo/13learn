# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df = pd.DataFrame({'foo': ['one','one','one','two','two','two'],
                               'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                               'baz': [1, 2, 3, 4, 5, 6]})

print df
df1 = df.pivot(index='foo',columns='bar',values='baz')
print df1
print df1.columns.name
index = pd.MultiIndex.from_tuples([('one', 'a'), ('one', 'b'),
	('two', 'a'), ('two', 'b')])

s = pd.Series(np.arange(1.0, 5.0), index=index)
print '---------------------------------'
print index
print '----'
print s
print '================================='
print s.unstack(level=-1)
print s.unstack(level=0)
print '+++++++++'
print s.unstack(level=0)


