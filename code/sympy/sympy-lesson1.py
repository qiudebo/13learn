# -*- coding:utf-8 -*-

'''
符号计算库
'''
from sympy import symbols
from sympy import series
from sympy import cos,sin
from sympy import integrate
from sympy import diff
from sympy import exp
from sympy import limit,oo
from sympy import solve
from sympy import expand

import numpy as np

x,y= symbols("x,y")
# 三角函数展开
print expand(sin(x+y),trig=True)

# 泰勒多项式展开

print series(sin(x),x,0,10)  

# 解方程组
a,b,c = symbols("a,b,c")
print solve(a*x**2 + b*x + c,x)

# 微分

# 积分





























