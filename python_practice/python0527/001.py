class Fibs():
    def __init__(self):
        self.a = 0
        self.b = 1
    # def __int__(self):
    #     self.a = 0
    #     self.b = 1
    def next(self):
        self.a,self.b = self.b,self.a + self.b
        return  self.a
    def iter(self):
        return  self
fibs = Fibs()
for i in Fibs():
    if i > 60000:
        print(i)
        break

# fib= Fibs('ab','ba')
#
# test = fib.next()
# testt = fib.iter()
# print(str(test) + str(testt))


