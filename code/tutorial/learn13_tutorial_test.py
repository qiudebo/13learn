#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

import time
import hashlib
import MySQLdb
import datetime
import pandas as pd
import numpy as np


if __name__ == '__main__':
    print time.localtime(time.time())
    print time.asctime(time.localtime(time.time()))
    print time.time()
    print int(time.time())
    print datetime.datetime.now()



