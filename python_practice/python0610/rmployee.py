class Employee():
    def __init__(self,first_name,last_name,sale):
        self.first_name = first_name
        self.last_name = last_name
        self.sale = sale
    def give_raise(self,value=5000):
        self.sale += value
