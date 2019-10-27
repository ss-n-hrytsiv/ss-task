from math import sqrt

__author__ = 'Maks Ivanov'

def task_num_243_b(n):
    """ b) Given a natural number n. Can it be represented as the sum of two squares of natural numbers?
        Indicate all pairs of numbers x, such natural numbers) """


    res = []

    for x in range(int(sqrt(n)) + 1):
        for y in range(x, int(sqrt(n)) + 1):
            if x ** 2 + y ** 2 == n:
                pair = f'{x} {y}'
                res.append(pair)
    if len(res) == 0:
        return "This number cannot be represented as the sum of two squares"
    return res


def task243_b_menu():
    while True:
        print('-' * 100)
        print('Function logic: ' + '\n' + task_num_243_b.__doc__)
        print('-' * 50)
        print('Input only number')
        print('If you wnat to exit, just input smth from: q /quit / exit /stop /terminate')
        print('-' * 50)

        user_number = input('\'Task 243b\' Input your natural number : ')
        try:
            m = int(user_number)
            print(task_num_243_b(m))
        except ValueError:
            if user_number.lower() in ['q', 'quit', 'exit', 'stop', 'terminate']:
                break

            print('n - must be an int type!')
            continue
