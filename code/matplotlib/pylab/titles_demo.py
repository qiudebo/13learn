#!/usr/bin/python
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt


if __name__ == '__main__':
    plt.plot(range(10))
    plt.title('Center Title')
    plt.title('Left Title', loc='left')
    plt.title('Right Title', loc='right')
    plt.show()