# 559
# Given natural n. Find all smaller n numbers of Mersenne.
import math
__author__ = 'Orest Furda'

def task_559(number):
    """Given natural n. Find all smaller n numbers of Mersenne."""

    num_mers = []
    counter = 1
    while True:
        expression = (2 ** counter - 1)
        if expression >= number:
            break
        num_mers.append(expression)
        counter += 1

    return num_mers


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
            num_mers = task_559(number)
            print(f'Numbers of Mersenne, less then {number} = {num_mers}')
            print('\n')
        except ValueError:
            if user_input_number.lower() in ['q', 'quit', 'exit', 'stop', 'terminate']:
                break
            print('n - must be an int type!')
            continue


if __name__ == "__main__":
    task_559_menu()
