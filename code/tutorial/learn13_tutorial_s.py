#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from bs4 import BeautifulSoup

import time
import hashlib
import urllib
import urllib2
from bs4 import Tag
import re
import pandas as pd
from pandas.io.excel import ExcelWriter


if __name__ == '__main__':
    #soup = BeautifulSoup(request, "html.parser")

    url = 'http://www.tutorialspoint.com/cordova/'
    url = 'http://www.tutorialspoint.com/mysql/'
    url = 'http://www.tutorialspoint.com/mongodb/'
    url = 'http://www.tutorialspoint.com/jenkins/'
    url = 'https://www.tutorialspoint.com/sqoop'
    # 文件名
    filename = 'sqoop'

    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    values = {'name': 'Michael Foord',
              'location': 'Northampton',
              'language': 'Python'}
    headers = {'User-Agent': user_agent}
    try:
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(req)
        the_page = response.read()
        soup = BeautifulSoup(the_page, "html.parser")

        # #方式1：
        districtInfos = soup.find('ul', attrs={'class': 'nav nav-list primary left-menu'})
        links = districtInfos.select('li > a')
        a = []
        b = []
        for link in links:
            #print link
            name = re.split(r'/',link['href'] + 'l')[2]
            value = re.split(r'_',name.replace('.html',''))
            if len(value) == 1:
                continue
            elif len(value)==2:
                a.append(name)
                b.append(value[0]+" "+value[1])
            elif len(value)==3:
                a.append(name)
                b.append(value[0] + " " + value[1] + " " + value[2])
            else:
                a.append(name)
                b.append(value[0] + " " + value[1] + " " + value[2]+ " "+ value[3])

        #方式2：
        s = pd.DataFrame(zip(a,b,b),columns=['url','keyword','description'])
        print s
        s.to_csv(filename+'.csv')
        # writer = ExcelWriter('output.xlsx')
        # s.to_excel(writer,sheet_name='cordova')
        # s.to_excel(writer,sheet_name='Sheet2')
        # writer.save()
    except urllib2.HTTPError, e:
        print e.code
        print e.reason
        print e.geturl()
        print e.read()
