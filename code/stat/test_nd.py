#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

import matplotlib.pyplot as plt
import tensorflow


x = np.array([8.7,9.7,9.9,9.9,9.9,10,10.1,10.1,16])
mu = 2
sigma=10.5
y = np.exp(-((x - mu)**2)/(2*sigma**2)) / (sigma * np.sqrt(2*np.pi))
print y

plt.plot(x,y)
plt.show()