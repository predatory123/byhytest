# 使用任意数量的关键数字实参
def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return  profile
user_profile = build_profile('永杰','文',年龄='21',身高='178',籍贯='四川')
print(user_profile)