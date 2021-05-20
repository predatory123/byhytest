'''
利用parse模块模拟post请求
分析百度词典
分析步骤：
      1.打开F12
      2.尝试输入单词 girl ，发现没敲一个字母后都有请求
      3.请求地址是:http://fanyi.baidu.com/sug
      4.利用Network-ALL-Hraders 查看，发现FormDate的值是: kw:girl

'''

from urllib import request,parse
import json

baseurl = "https://fanyi.baidu.com/sug"
#存放用来模拟from的数据一定是dict格式
data = {
    #  girl是翻译输入的英文内容，应该是由用户输入，此处使用硬解码
    'kw':'girl'
}

#需要使用parse模块对date进行解码
data = parse.urlencode(data).encode('utf-8')
print(type(data))

# 我们需要构造一个请求头，包含传入数据的长度
# request要求传入的请求体是dict格式
headers = {
    #因为使用post，至少应该包含content-length字段
    'Content-Lengh':len(data)
}

# 有了herders.date.url,就可以尝试着发出请求了
rsp = request.urlopen(baseurl, data=data)

json_data = rsp.read().decode('utf-8')
print( type(json_data))
print(json_data)

# 把json字符串转化为字典
json_data = json.loads(json_data)
print(type(json_data))
print(json_data)

for item in json_data['data']:
    print(item['k'], '--', item['v'])