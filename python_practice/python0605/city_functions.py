# class city_function():
    # def __init__(self,city,country):
    #     self.city = city
    #     self.country = country
def value(city,country,population):
        # self.city = city
        # self.country = country
        # self.poulation = population
    test = city.title()+','+country.title()+'_'+str(population) + ' people.'
    return test


name = value('chengdu','china',50)
print(name)