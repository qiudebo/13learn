#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    plt.plot([1,2,3,4],[1,4,9,16],'ro',linewidth=2.0)
    plt.axis([0,6,0,20])
    plt.suptitle("test")
    plt.title("title")
    plt.show()


    t = np.arange(0., 5., 0.2)
    print t
    t1 = np.linspace(5,10)
    t2 = np.linspace(10,20)
    print t1

    plt.plot(t, t*2,'g--', t1, t1*2,'bs', t2, t2*2,'r^')

    #plt.show()
