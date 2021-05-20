# 导入 json模块
import json

number = [1,2,3,4,5,6,7,8,9]
filename = 'number.json'
with open(filename,'w') as f_obj:
    json.dump(number,f_obj)