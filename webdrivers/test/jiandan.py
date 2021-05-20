# # -*- coding:utf-8 -*-
# '''
# version:Python 2.6
# standard libs: urllib
# author:Dead_morning
# system: cetos 6.5
# '''
# import re
# import urllib
#
# def get_content(html_page):
#  '''html downladd'''
#     html = urllib.urlopen(html_page)
#     content = html.read()
#     html.close()
#     return content
#
# def get_images(info):
# '''html parser'''
#     regex = r'href="//wx(.+?\.(?:gif|jpg|jpeg|png))" ' # download original picture
#     #使用正则表达式为了下载原图，这里可使用 soupbeautiful 模块替代正则表达式
#     pat = re.compile(regex)
#     image_code = map(lambda x: 'http://wx'+ x , re.findall(pat,info))
#     return image_code
#
# def Download_image():
# ''' image download'''
#     for image_url in get_images(info):
#         print image_url
#         image_name = image_url.split('/')[-1]
#         # 给文件命名
#         urllib.urlretrieve(image_url,image_name)
#
# def html_pages():
# ''' URl list'''
# #因为煎蛋网的网址比较有规律，所以就用了一个简单的List替代了从网页里解析
#     b = []
#     for a in range (1 ,95):
#         url= 'http://jandan.net/ooxx/page-%s#comments' %a
#         b.append(url)
#     return b
#
# if __name__ == '__main__':
#     for html_page in html_pages():
#         info = get_content(html_page)
#         print Download_image()


# coding=utf-8

import requests
from bs4 import BeautifulSoup


# 获取html文档
def get_html(url):
    """get the content of the url"""
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text


# 获取笑话
def get_certain_joke(html):
    """get the joke of the html"""
    soup = BeautifulSoup(html, 'lxml')
    joke_content = soup.select('div.content')[0].get_text()

    return joke_content


url_joke = "https://www.qiushibaike.com"
html = get_html(url_joke)
joke_content = get_certain_joke(html)
print
joke_content
