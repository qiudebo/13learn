# uniform distribution

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


# s = np.random.uniform(-1,0,1000)
# print len(s)
# np.all(s>=-1)
# np.all(s<0)
# count, bins, ignored = plt.hist(s, 15, normed=True)
# print count
# print bins
# print ignored
# plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
# plt.show()
n, p = 10, .3
k = np.arange(0,10)
s = stats.binom.pmf(k, n, p)
print s
