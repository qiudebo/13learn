
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols
from sympy import limit

if __name__ == '__main__':
	x = np.random.randn(1000)
	y = np.arange(1001)
	# plt.plot(x)
	# plt.show()
	print y

	s = np.random.dirichlet((10, 5, 3), 20).transpose()
	print '--------------------------------------------'
	print s
    
    x = symbols('x') 
    print limit((x**3-1)/(x**2-5*x+3), x, 2)