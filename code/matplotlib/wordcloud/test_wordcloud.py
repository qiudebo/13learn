#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'qiudebo'


from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import chardet                         #检测字符类型的类
import json
from scipy.misc import imread
import os
from os import path
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import jieba

if __name__ == '__main__':
    # color_mask = imread("Anne_Hathaway.png")  # 读取背景图片

    #data = {u"乐视": 10, u"爱奇艺": 30, u"优酷": 5, u"腾讯": 4, u"土豆": 50}

    # Generate a word cloud image
    data = open('data').read().decode('utf-8')
    data1 = json.dumps(data)
    font = os.path.join(os.path.dirname(__file__), "D://letvworkspace//DroidSansFallbackFull.ttf")
    #wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)
    #wl_space_split = " ".join(wordlist_after_jieba)

    # 设置背景色
    # 设置字体 font_path  font_path=path.join(d,'simsun.ttc'),

    backgroud_Image = plt.imread('test2.jpg')

    #backgroud_Image = np.array(Image.open("test.jpg"))
    print backgroud_Image

    # 词云形状 mask
    # 允许最大词汇 max_words = 2000
    # 最大号字体 max_font_size=40

    #
    # wordcloud = WordCloud(max_font_size=40, background_color="black",
    #                       width=300,height=400,margin=2
    # )
    wordcloud = WordCloud(font_path=font,
                          background_color='white',
                          mask=backgroud_Image,
                          width=100,
                          height=100)
    # 产生词云

    # 生成词云, 可以用generate输入全部文本(中文不好分词),也可以我们计算好词频后使用generate_from_frequencies函数
    # 文本词频统计函数，本函数自动统计词的个数，以字典形式内部存储，在显示的时候词频大的，字体也大

    wordcloud.generate(data)

    # 从背景图片生成颜色值
    image_colors = ImageColorGenerator(backgroud_Image)

    wordcloud.to_file("rr.jpg")  # 保存图片
    plt.figure()

    #显示词云图片
    #plt.imshow(wordcloud.recolor(color_func=image_colors))
    plt.imshow(wordcloud)
    # 不显示坐标
    plt.axis("off")

    plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.show()



