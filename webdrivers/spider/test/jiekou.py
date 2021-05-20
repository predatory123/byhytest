import requests,pprint

print('测试登录----------------------------------------------------')
payload = {
    'username': 'test',
    'password': '88888888'
}

response = requests.post('http://127.0.0.1:8000/api/mgr/signin',
              data=payload)

# print(response.cookies.get_dict())
sessionid = response.cookies['sessionid']
cookies = {
    'sessionid':sessionid
}

pprint.pprint(response.json())

response1 = requests.get('http://127.0.0.1:8000/api/mgr/customers?action=list_customer', cookies=cookies)
print('列出所有的客户------------------------------------')
pprint.pprint(response1.json())

# 构建添加 客户信息的 消息体，是json格式
payload = {
    "action": "add_customer",
    "data": {
        "name": "武汉市桥西医院",
        "phonenumber": "13345679934",
        "address": "武汉市桥西医院北路"
    }
}

# 发送请求给web服务
response = requests.post('http://127.0.0.1:8000/api/mgr/customers',
                         json=payload,cookies=cookies)
print('添加客户'+ '='*50)
pprint.pprint(response.json())

pyload1 = {
     "action":"modify_customer",
     "id": 28,
     "newdata":{
         "name":"杭州市邵逸夫医院",
         "phonenumber":"13345678888",
         "address":"杭州市桥邵逸夫医院"
     }
 }

response1 = requests.post('http://127.0.0.1:8000/api/mgr/customers',
                           json=pyload1,cookies=cookies)
print('修改客户'+ '='*50)
pprint.pprint(response1)

print('删除客户')
pyload2 = {
    "action":"del_customer",
    "id": 29
}

response2 = requests.post('http://127.0.0.1:8000/api/mgr/customers',
                         json=pyload2)
pprint.pprint(response2)
