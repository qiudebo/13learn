#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import matplotlib.pyplot as plt

vals1 = [1, 2, 3, 4]
vals2 = [2, 3, 4, 5]
fig, ax = plt.subplots()
labels = 'A', 'B', 'C', 'D'
ax.pie(vals1, radius=1.2,autopct='%1.1f%%',pctdistance=0.9)
ax.pie(vals2, radius=1,autopct='%1.2f%%',pctdistance=0.5)
ax.set(aspect="equal", title='Pie plot with `ax.pie`')
#plt.legend()
plt.legend(labels,bbox_to_anchor=(1.05, 1), loc='best', borderaxespad=0.)
plt.show()