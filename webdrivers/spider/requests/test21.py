import requests

url = 'http://www.baidu.com'

# 第一种，requests.get()
rsp = requests.get(url)
print(rsp.text)

# 第二种，requests.request
req = requests.request('get',url)
print(req.text)