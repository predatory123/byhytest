cities = {'chengdu':{'country':'china','population':13000,'fact':'funny'},
          'new_york':{'country':'America','population':2000,'fact':'free'},
          'london':{'country':'England','population':1000,'fact':'gentleman'},

          }
for city,city_people in cities.items():
    country = city_people['country']
    population = city_people['population']
    fact = city_people['fact']
    print(city + ' is in ' + country + ','+ 'and have'+ str(population) + 'people'+ ','+'and they feel'+ fact)
    print(city,country,population,fact)



