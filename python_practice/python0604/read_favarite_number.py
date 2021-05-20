import json

love = 'value.json'
with open(love) as f_obj:
    number = json.load(f_obj)
    print(number)
