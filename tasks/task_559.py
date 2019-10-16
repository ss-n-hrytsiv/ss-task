# 559
# Дано натуральне n. Знайти всі, менші n числа Мерсенна.
import math
__author__ = 'Orest Furda'

def task_559(n):
    """Дано натуральне n. Знайти всі, менші n числа Мерсенна."""
    # n = input("Enter n: ")
    num_mers = [(2 ** i - 1) for i in range(1, n + 1)]
    simple_num = []

    # for i in range(1, n+1):
    #     num_mers.append(2 ** i - 1)

    for count in range(2, n+1):
        i = 2
        limit = int(math.sqrt(count))
        while i <= limit:
            if count % i == 0:
                break
            i += 1
        else:
            simple_num.append(count)
    simple_num_mers = [(2 ** i + 1) for i in simple_num]
    # for i in simple_num:
    #     simple_num_mers.append(2 ** i - 1)

    return num_mers, simple_num_mers


def task_559_menu():
    while True:
        print('-' * 100)
        print('Function logic: ' + '\n' + task_559.__doc__)
        print('-' * 50)
        print('-' * 100)
        print('Input only number')
        print('If you wnat to exit, just input smth from: q /quit / exit /stop /terminate')
        print('-' * 50)
        print('\n')
        user_input_n = input('Please input a number(n): ')

        try:
            n = int(user_input_n)
            num_mers, simple_num_mers = task_559(n)
            print(f'Числа Мерсенна, менші за {n} = {num_mers}')
            print(f'Прості числа Мерсенна, менші за {n} = {simple_num_mers}')
            print('\n')
        except ValueError:
            if user_input_n.lower() in ['q', 'quit', 'exit', 'stop', 'terminate']:
                break
            print('n - must be an int type!')
            continue


if __name__ == "__main__":
    task_559_menu()
