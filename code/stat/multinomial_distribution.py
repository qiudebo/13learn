#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

if __name__ == '__main__':
    np.random.multinomial(20, [1 / 6.] * 6, size=1)
    np.random.multinomial(20, [1 / 6.] * 6, size=2)
    np.random.multinomial(100, [1 / 7.] * 5 + [2 / 7.])
    np.random.multinomial(100, [1.0 / 3, 2.0 / 3])
    np.random.multinomial(100, [1.0, 2.0])