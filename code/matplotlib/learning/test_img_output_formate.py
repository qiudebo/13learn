#!/usr/bin/python
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
from matplotlib import rcsetup

import pandas as pd



if __name__ == '__main__':

    print rcsetup.all_backends


    iris = pd.read_csv('iris.csv')
    