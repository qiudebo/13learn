#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'


from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


def binom_dist_plot():
    '''
    模拟泊松分布 
    :return: 
    '''
    n = 10
    p = 0.5
    k = np.arange(0, 21)
    print k
    binomial = stats.binom.pmf(k, n, p)
    print binomial
    print plt
    plt.title('Binomial:n=%i, p=%.2f' % (n, p), fontsize=15)
    plt.xlabel('Number of success')
    plt.ylabel('Probability of success', fontsize=15)
    plt.plot(k, binomial, 'o-')
    plt.show()

def binom_dist_hist():
    '''
    模拟泊松分布-直方图
    :return: 
    '''
    n = 10
    p = 0.3
    size = 10000
    binom_sim = stats.binom.rvs(n=10, p=0.3, size=10000)
    print binom_sim
    print 'Mean:%g' % np.mean(binom_sim)
    print 'Std:%g' % np.std(binom_sim, ddof=1)
    plt.hist(binom_sim, bins=10, normed= True)
    plt.xlabel("x")
    plt.ylabel("density")
    plt.show()

def possion_dist_plot():
    rate = 2
    n = np.arange(0, 10)
    print n
    y = stats.poisson.pmf(n, rate)
    print y
    plt.title('Possion:rate=%s'%rate)
    plt.xlabel("Numbers of accidents")
    plt.ylabel("Probability of number of accidents")
    plt.plot(n, y, 'o-')
    plt.show()

def possion_dist_hist():
    data = stats.poisson.rvs(mu=2, loc=0, size=1000)
    print data
    print 'Mean: %g'%np.mean(data)
    print 'Sd: %g'%np.std(data,ddof=1)
    plt.figure()
    plt.hist(data, bins=9, normed=True)
    plt.xlim(0,10)
    plt.xlabel('Numbers of accidents')
    plt.title('Simulating Possion Random Variables')
    plt.show()

def normal_dist_plot():
    mu = 0
    sigma = 1
    x = np.arange(-5,5,0.1)
    print x
    y = stats.norm.pdf(x,0,1)
    plt.plot(x,y)
    plt.title('Normal:$\mu$=%.1f, $\sigma^2=%.1f$'%(mu,sigma))
    plt.xlabel('x')
    plt.ylabel('Probability distribution')
    plt.show()

def beta_dist_plot():
    a=0.5
    b=0.5
    x=np.arange(0.01,1,0.01)
    y=stats.beta.pdf(x,a,b)
    plt.plot(x,y)
    plt.title('Beta a=%.1f,b%.1f'%(a,b))
    plt.xlabel('x')
    plt.ylabel('Probability density')
    plt.show()

def exponential_dist_plot():
    lambd = 0.5
    x = np.arange(0,15,0.1)
    y = lambd*np.exp(-lambd*x)
    print y
    plt.plot(x,y)
    plt.title('Exponential:$\lambda$=%.2f'%lambd)
    plt.xlabel('x')
    plt.ylabel('Probability density')
    plt.show()

def exponential_dist_hist():
    data = stats.expon.rvs(scale=2,size=1000)
    print 'Mean:%g'%np.mean(data)
    print 'SD:%g'%np.std(data,ddof=1)
    plt.figure()
    plt.hist(data,bins=20,normed=True)
    plt.xlim(0,15)
    plt.title("Simulating Exponential Random Variables")
    plt.show()


if __name__ == '__main__':
    #binom_dist_plot()
    #binom_dist_hist()
    #possion_dist_plot()
    #possion_dist_hist()
    #normal_dist_plot()
    #beta_dist_plot()
    exponential_dist_plot()
    #exponential_dist_hist()
if __main__ == '__main__':






