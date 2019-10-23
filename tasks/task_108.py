"""
python 3.7
author: Andrew Stanishevskyi
"""


def task_108(input_data):
    """
    Дано натуральное число n. Получить наименьшее число
    вида 2^r , превосходящее n.
    """
    if isinstance(input_data, int):
        if input_data > 0:
            for i in range(input_data + 1):
                two_to_i_power = 2 ** i
                if two_to_i_power > input_data:
                    return two_to_i_power
        else:
            print('n must be bigger than 0')
    else:
        raise Exception('Type integer')


def task_108_menu():
    print('-' * 100)
    print(f'Function logic:\n{task_108.__doc__}')
    print('-' * 50)
    print("Input some integer number:\n")
    try:
        input_data = int(input())
        print(f'Result: {task_108(input_data)}')
    except Exception as error:
        print(f'{error}. Try again!'.title())


if __name__ == '__main__':
    task_108_menu()
