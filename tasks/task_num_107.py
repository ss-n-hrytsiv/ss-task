""" We have a natural number m > 1. Get the greatest integer k, at which 4^k < m
"""


def task_num_107(abra):
    """ Дано целое число m > 1 Получить наибольшое целое к, при котором 4^к < m
        (We have a natural number m > 1. Get the greatest integer k, at which 4^k < m)
    """
    counter = 1
    a = 4
    while a < abra:
        a *= a
        counter += 1
    return counter


def task107_menu():
    while True:
        print('-' * 100)
        print('Function logic: ' + '\n' + task_num_107.__doc__)
        print('-' * 50)
        print('Input only number')
        print('If you wnat to exit, just input smth from: q /quit / exit /stop /terminate')
        print('-' * 50)

        user_number = input('\'Task 107\' Input your natural number : ')
        try:
            m = int(user_number)
            print(task_num_107(m))
        except ValueError:
            if user_number.lower() in ['q', 'quit', 'exit', 'stop', 'terminate']:
                break

            print('n - must be an int type!')
            continue
