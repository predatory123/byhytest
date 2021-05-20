import requests

url = 'http://www.baidu.com/s?'

kw = {
    'wd':'大熊猫'
}

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

rsp = requests.get(url,params=kw,headers=headers)
print(rsp.text)
print(rsp.content)
print(rsp.encoding)
print(rsp.status_code)