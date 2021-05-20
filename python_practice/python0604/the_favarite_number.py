import json

love = 'value.json'
try:
    with open(love) as f_obj:
        value = json.load(f_obj)
        print('I know you favorite number! it\'s___'+ value)
except FileNotFoundError:
    value = input('请输入你最喜欢的数字：')
    # love = 'value.json'
    with open(love,'w') as f_obj:
        json.dump(username, f_obj)
        print('I know you favorite number! it\'s___'+ username)
# else:
#     print(None)