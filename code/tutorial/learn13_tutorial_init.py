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

    #content = [parentid, cateid, title, keywords, description, url, username]
    try:
        conn = MySQLdb.connect(host="", user="", port=, passwd="", db="", charset="utf8")
        cursor = conn.cursor()
    except Exception as e:
        print e
        driver.quit()
        cursor.close()
    # 文件名
    filename = 'sqoop'
    # 先查询此是否已经存在该分类的教程
    sql = "select cateid from category where catename like '%sqoop%' and child = 0"

    count = cursor.execute(sql)
    print count
    #result = cursor.fetchall()
    result = cursor.fetchone()

    cateid = result[0]

    sql = "select id from knowledge where cateid=%s" % cateid
    count = cursor.execute(sql)
    if count >0:
        print '====================该教程提纲已经存在！！！====================='
    #如果不存在，则读取csv格式提纲
    if count ==0:
        parentid = 0    # 默认 0 表示 一级
        username = 'qb' # 默认录入用户
        thumb = ''
        title = ''       # 标题
        keywords = ''    # 关键词
        description = '' # 摘要
        url = ''         # 路径关键词

        # 读取教程提纲
        data = pd.read_csv(filename+'.csv', encoding='GBK')
        print len(data)

        #此处为打印csv内容  可忽略
        for i in range(len(data)):
            print '=='
            print data.loc[i]['title'],data.loc[i]['url'],data.loc[i]['keyword'],data.loc[i]['description']
        listorder = 0
        # 将提纲信息插入教程主表 knowledge
        for index, row in data.iterrows():
            print '---'
            title = row.title
            keywords = row['keyword'] + " " + row['title2']
            description = keywords
            url = row['url']
            inputtime = int(time.time())
            listorder = listorder + 1
            sql = "insert into knowledge(parentid, cateid, title, thumb,keywords,description,url,username,listorder)" \
                  " values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            param = (parentid, cateid, title, thumb, keywords, description, url, username,listorder)
            n = cursor.execute(sql, param)
        # 查询教程主表的提纲数目
        sql = "select id from knowledge where cateid=%s" % cateid
        content = "1"
        count = cursor.execute(sql)
        print count
        result = cursor.fetchall()
        # 根据教程主表的提纲初始化教程内容表，内容初始化为"1"
        for r in result:
            line = r[0]
            sql = "insert into knowledge_data(id,content) values(%s,%s)"
            param = (line, content)
            n = cursor.execute(sql, param)
    cursor.close()





