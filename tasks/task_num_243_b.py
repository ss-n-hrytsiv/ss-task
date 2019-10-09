from math import sqrt


def task_num_243_b():
    """ Дано натуральное число n. Можно ли представить его в виде суммы двух квадратов натуральных чисел?
        б) указать все пары чисел х, у таких натуральных чисел, что n = x^2 + y^2 """

    res = []
    n = int(input("\'Task 243 b\' Input your natural number : "))
    for x in range(int(sqrt(n)) + 1):
        for y in range(x, int(sqrt(n)) + 1):
            if x ** 2 + y ** 2 == n:
                pair = f'{x} {y}'
                res.append(pair)
    if len(res) == 0:
        return "This number cannot be represented as the sum of two squares"
    return res