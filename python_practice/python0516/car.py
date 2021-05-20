def cars_message(name,country,**speed):
    cars_name = {}
    cars_name['name_message'] = name
    cars_name['country_message'] = country
    for key,value in speed.items():
        cars_name[key] = value
    return cars_name

car = cars_message('Audi','Germany',color='blue',horsepower='350',engin='V6 twin turbocharged engine')
print(car)
