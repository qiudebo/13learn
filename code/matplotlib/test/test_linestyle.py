#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines

class HighlightSelected(lines.VertexSelector):
    def __init__(self, line, fmt='ro', **kwargs):
        lines.VertexSelector.__init__(self, line)
        self.markers, = self.axes.plot([], [], fmt, **kwargs)

    def process_selected(self, ind, xs, ys):
        self.markers.set_data(xs, ys)
        self.canvas.draw()

if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x, y = np.random.rand(2, 30)
    line, = ax.plot(x, y, 'r,-', picker=5)

    selector = HighlightSelected(line)
    plt.show()