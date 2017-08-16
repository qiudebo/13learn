#!/usr/bin/python
# -*- coding: utf-8 -*-


import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

if __name__ == '__main__':

    b = random.binomial(5, 0.5, size=15)
    print b

    # n = 5
    # p=0.5
    #
    # s = np.random.binomial(n, p, 1000)
    # print s

    mu, sigma = 0, 0.5  # mean and standard deviation
    s = np.random.normal(mu, sigma, 1000)
    print abs(mu - np.mean(s)) < 0.01
    print abs(sigma - np.std(s, ddof=1)) < 0.01
    # probability density function:
    #PDF

    count, bins, ignored = plt.hist(s, 30, normed=True)
    print '-----'
    print count
    print bins
    print ignored

    for sigma1 in [0.5,1.0,1.5]:
        plt.plot(bins, 1 / (sigma1 * np.sqrt(2 * np.pi)) * np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)), linewidth=2, color='r')

    #plt.show()



