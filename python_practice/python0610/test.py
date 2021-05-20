import unittest
from rmployee import Employee

class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        '''创建一个调查对象和一组答案，供使用的测试方法使用'''
    question = 'What people did you want? '
    my_employee = Employee('taylor','swift',5000)

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 15000)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(10000)
        self.assertEqual(self.my_employee.salary, 20000)



unittest.main()


