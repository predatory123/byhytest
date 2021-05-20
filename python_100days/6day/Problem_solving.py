# 在讲解本章节的内容之前，我们先来研究一道数学题，请说出下面的方程有多少组正整数解。
#                  x1 + x2 + x3 + x4 = 8
# 事实上，上面的问题等同于将8个苹果分成四组每组至少一个苹果有多少种方案。想到这一点问题的答案就呼之欲出了。
#
# 可以用Python的程序来计算出这个值，代码如下所示。

# """
# 输入M和N计算C(M,N)
# """
#
# m = int(input('m = '))
# n = int(input('n = '))
# fm = 1
# for num in range(1, m + 1):
#     fm *= num
# fn = 1
# for num in range(1, n + 1):
#     fn *= num
# fmn = 1
# for num in range(1, m - n + 1):
#     fmn *= num
# print(fm // fn // fmn)

def factorial(num):
    """
    求阶乘

    :param num: 非负整数
    :return: num的阶乘
    """
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


m = int(input('m = '))
n = int(input('n = '))
# 当需要计算阶乘的时候不用再写循环求阶乘而是直接调用已经定义好的函数
print(factorial(m) // factorial(n) // factorial(m - n))