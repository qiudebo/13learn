# -*-coding:utf-8 -*-


import numpy as np
from numpy import linalg as LA


x = np.array([1,2,3])
y = np.array([1,2,-5/3])
print LA.norm(x)
print np.dot(x,y)
print np.arccos(np.dot(x,y)/(LA.norm(x)*LA.norm(y)))*180/np.pi

