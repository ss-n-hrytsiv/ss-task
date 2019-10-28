from math import sqrt

__author__ = 'Maks Ivanov'

def task_num_243_a(n):
    """ Дано натуральное число n. Можно ли представить его в виде суммы двух квадратов натуральных чисел?
        a) указать пару чисел х, у таких натуральных чисел, что n = x^2 + y^2
        (Given a natural number n. Can it be represented as the sum of two squares of natural numbers?
        indicate a pair of numbers x, such natural numbers that for n = x^2 + y^2) """

    res = []
    for x in range(int(sqrt(n)) + 1):
        for y in range(x, int(sqrt(n)) + 1):
            if x ** 2 + y ** 2 == n:
                pair = (x, y)
                res.append(pair)
    if len(res) == 0:
        return "This number can not be represented as the sum of two squares"
    return res[0]


def task243_a_menu():
    while True:
        print('-' * 100)
        print('Function logic: ' + '\n' + task_num_243_a.__doc__)
        print('-' * 50)
        print('Input only number')
        print('If you wnat to exit, just input smth from: q /quit / exit /stop /terminate')
        print('-' * 50)

        user_number = input('\'Task 243a\' Input your natural number : ')
        try:
            n = int(user_number)
            print(task_num_243_a(n))
        except ValueError:
            if user_number.lower() in ['q', 'quit', 'exit', 'stop', 'terminate']:
                break

            print('n - must be an int type!')
            continue