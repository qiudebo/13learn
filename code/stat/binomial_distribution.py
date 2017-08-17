#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd

if __name__ == '__main__':
    n, p = 10, .5  # number of trials, probability of each trial
    s = np.random.binomial(n, p)
    print s
    plt.hist(s)
    k = np.arange(0,21)
    print stats.binom.pmf(k,10,0.5)
    # plt.show()

    stats.binom.rvs()