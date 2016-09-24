#!/usr/bin/env python
# coding=utf-8

__author__ = 'lideqiang87@gmail.com'

import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    #print html
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    print imglist
    x = 0
    for imgurl in imglist:
        #print imgurl  
        urllib.urlretrieve(imgurl, 'img/%s.jpg' % x)
        x+=1

html = getHtml("http://tieba.baidu.com/p/2460150866")
print getImg(html)
