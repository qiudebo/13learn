# *-* coding:utf-8 *-*

import pandas as pd
import csv
import urllib2

# 数据集 https://vincentarelbundock.github.io/Rdatasets/datasets.html
# http://forge.scilab.org/index.php/p/rdataset/source/tree/master/csv

url = "http://forge.scilab.org/index.php/p/rdataset/source/file/master/csv/car/Soils.csv"
res = urllib2.urlopen(url)
data = csv.reader(res)
for line in data:
	print line








