# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


if __name__ == '__main__':
	print np.zeros((5,))
	print np.zeros((2,), dtype=[('x', 'i4'), ('y', 'i4')])
	print np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
	xs = np.linspace(0, 2*np.pi, 100)
	ys = np.sin(xs)
	plt.plot(xs, ys)
	plt.plot(ys, xs)
	#plt.show()
	n, p = 10, .5
	s = np.random.binomial(n, p, 1000)
	c = Counter(s)
	print list(c.elements())
	print np.sum(s)/10000.00
	print type(s)
	plt.hist(s)
	plt.show()
