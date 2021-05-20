import unittest
from city_functions import value
# 创建 一个用于单元测试的类
class city_test(unittest.TestCase):
    def test_city_country(self):
#验证 是否能够正确处理 city 和 country 的值
        true_name = value('shanghai','china')
        self.assertEqual(true_name,'Shanghai China')
unittest.main()
