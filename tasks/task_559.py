# 559
# Given natural n. Find all smaller n numbers of Mersenne.
import math
__author__ = 'Orest Furda'

def task_559(number):
    """Given natural n. Find all smaller n numbers of Mersenne."""

    num_mers = [(2 ** i - 1) for i in range(1, number + 1)]
    simple_num = []

    for count in range(2, number+1):
        i = 2
        limit = int(math.sqrt(count))
        while i <= limit:
            if count % i == 0:
                break
            i += 1
        else:
            simple_num.append(count)
    simple_num_mers = [(2 ** i + 1) for i in simple_num]
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

        user_input_number = input('Please input a number(n): ')

        try:
            number = int(user_input_number)
            num_mers, simple_num_mers = task_559(number)
            print(f'Numbers of Mersenne, less then {number} = {num_mers}')
            print(f'Simple numbers of Mersenne, less then {number} = {simple_num_mers}')
            print('\n')
        except ValueError:
            if user_input_number.lower() in ['q', 'quit', 'exit', 'stop', 'terminate']:
                break
            print('n - must be an int type!')
            continue


if __name__ == "__main__":
    task_559_menu()
