# 导入json模块
import  json

filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input('what\' your name ? -- ')
    with open(filename,'w') as f_obj:
        json.dump(filename,f_obj)
        print('We\'ll rememeber you when you come back,' + username +'!')
else:
    print('Welcome back,'+ username + '!')

