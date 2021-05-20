from random import randint

class Die():
    def __init__(self):
        self.sides = 10
    def roll_die(self):
        x = randint(1, 6)
        self.sides = x
        print(self.sides)
    def roll_die10(self):
        x = randint(1, 10)
        self.sides = x
        print(self.sides)
    def roll_die20(self):
        x = randint(1,20)
        self.sides = x
        print(self.sides)

die = Die()
print('--------开始了！6个面的色子:')
for i in range(10):
    die.roll_die()

print('--------开始了！10个面的色子:')
for i in range(10):
    die.roll_die()

print('--------开始了！20个面的色子:')
for i in range(10):
    die.roll_die()