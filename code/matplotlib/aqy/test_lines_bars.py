#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    plt.rcdefaults()
    fig, ax = plt.subplots()
    people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
    y_pos = np.arange(len(people))
    print y_pos
    performance = 3 + 10 * np.random.rand(len(people))
    error = np.random.rand(len(people))
    ax.barh(y_pos, performance, xerr=error, align='center',
            color='green', ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(people)
    ax.invert_yaxis()
    ax.set_xlabel('Performance')
    ax.set_title('How fast do you want to go today?')
    plt.savefig("test_lines_bars.png")
    plt.show()