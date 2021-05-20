import requests

urlpara = {
    'wd':'iphone&ipad'
    'rsv_spt':'1'
                     }

response = requests.get('https://www.baidu.com/s',params=urlpara)
# response = requests.get('https://www.baidu.com/s?wd=iphone&rsv_spt=1')
print(response.text)