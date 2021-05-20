#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from selenium import  webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)

# ================================================
# open URL
driver.get('https://www.baidu.com/')

ele = driver.find_element_by_tag_name("html")
html_doc = ele.get_attribute('innerHTML')

#
# BeautifulSoup
#
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, "html5lib")

# title
print('==title=='*4)
print(soup.find('title'))
print(soup.title)
print(soup.title.string)

# get tag name
print('==tag=='*4)
print(soup.title.name)
print(soup.find('title').name)

# get tag text
print('==tag text=='*4)
print(soup.title.string)
print(soup.title.get_text())

# get web element attribute value
print('==tag attribute value=='*4)
print(soup.div['id'])
print(soup.div['style'])
print(soup.div.get('style'))

# get the first tag a
print(soup.find('a'))

# get all tag a
# return a list, then get specified tag by list index
# print(soup.find_all('a'))
print(soup.find_all('a')[2]) # third tag

# by tag and attribute
print('==tag and attribute =='*4)
print(soup.find('input', id="su"))

# ================================================
input('Please input any key to continue......')
# Quit
driver.quit()


