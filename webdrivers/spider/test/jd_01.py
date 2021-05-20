import requests
from bs4 import BeautifulSoup
import re
url = 'https://maoyan.com/query?'

data = {
    'kw':'功夫熊猫'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
req = requests.get(url,params=data,headers=headers)
rsp = req.text
# print(rsp)

soup = BeautifulSoup(rsp, 'lxml')
# print(soup.dd.text)

value = soup.dd.text
print(value)
#









