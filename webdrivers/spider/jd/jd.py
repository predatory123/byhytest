import urllib.request
import requests
from bs4 import BeautifulSoup
import os
import re


id = 1
while(id < 400):
    id += 1
    try:
        headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
        resp = requests.get('https://search.jd.com/Search?keyword=iphone%20x&enc=utf-8'
                            '&suggest=1.rem.0.V10--12s0,20s0,38s0&wq=iphone%20x'
                            '&pvid=e434d920f70640c781463fe9c6f44f07' + str(id) + '/',headers=headers)
        html_doc =resp.text
        print(html_doc)

        soup = BeautifulSoup(html_doc,'lxml')
        print(soup)
        recipe_name = soup.find(target="_blank").get('title')
        print(recipe_name)
        img_html = soup.find(target="_blank").get('src')
        print(img_html)
    except Exception as e:
        print(e)
    else:
        continue




