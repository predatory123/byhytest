import requests
from bs4 import BeautifulSoup

url = 'https://maoyan.com/films/78535'
req = requests.get(url)
# print(req.text)

soup = BeautifulSoup(req.text, 'lxml')
print(soup.h3.get_text())
print(soup.h3.string)

# for link in soup.find_all('div'):
#     print(link.get_text())

# value_name = soup.find()
# print(value_name)