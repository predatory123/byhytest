import json

value = input('请输入你最喜欢的数字：')
love = 'value.json'
with open(love,'w') as f_obj:
    json.dump(value,f_obj)
    # print('I know you favorite number! it\'s___'+ value)



