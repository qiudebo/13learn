#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    mu, sigma = 0, 0.1  # mean and standard deviation
    s = np.random.normal(mu, sigma, 1000)
    abs(mu - np.mean(s)) < 0.01  # Verify the mean and the variance
    abs(sigma - np.std(s, ddof=1)) < 0.01

    # 画样本服从该分布的概率密度的直方图

    count, bins, ignored = plt.hist(s, 30, normed=True)
    plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) *
             np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)),
             linewidth=2,
             color='r')
    plt.show()
