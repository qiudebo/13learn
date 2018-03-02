# -*- coding:utf-8 -*-


import numpy as np

# 打印下三角形
# 打印上三角形
n = np.arange(1,10)
for i in n:
	j = i
	for j in n:
		if j<=i:
			print j,
		else:
			print " ",
	print "\n"

print '====================='

for i in n:
	j = i
	for j in n:
		if j>=i:
			print j,
		else:
			print " ",
	print "\n"


print '====================='

# 打印九九乘法表
for i in n:
	j = i
	for j in n:
		if j>=i:
			print i," * ",j," = ",j*i,";",
		else:
			print " ",
	print "\n"



