from math import sqrt


def task_num_107():
    """ Дано целое число m > 1 Получить наибольшое целое к, при котором 4^к < m """
    m = int(input('\'Task 107\' Input your natural number : '))
    counter = 1
    a = 4
    while a < m:
        a *= a
        counter += 1
    return counter


def task_num_243_a():
    """ Дано натуральное число n. Можно ли представить его в виде суммы двух квадратов натуральных чисел?
        a) указать пару чисел х, у таких натуральных чисел, что n = x^2 + y^2 """

    n = int(input("\'Task 243 a\' Input your natural number : "))
    res = []
    for x in range(int(sqrt(n)) + 1):
        for y in range(x, int(sqrt(n)) + 1):
            if x ** 2 + y ** 2 == n:
                pair = (x,y)
                res.append(pair)
    if len(res) == 0:
        return "This number can not be represented as the sum of two squares"
    return res[0]


def task_num_243_b():
    """ Дано натуральное число n. Можно ли представить его в виде суммы двух квадратов натуральных чисел?
        б) указать все пары чисел х, у таких натуральных чисел, что n = x^2 + y^2 """

    res = []
    n = int(input("\'Task 243 b\' Input your natural number : "))
    for x in range(int(sqrt(n)) + 1):
        for y in range(x, int(sqrt(n)) + 1):
            if x ** 2 + y ** 2 == n:
                pair = (x,y)
                res.append(pair)
    if len(res) == 0:
        return "This number cannot be represented as the sum of two squares"
    return res



