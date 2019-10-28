"""
python 3.7
author: Andrew Stanishevskyi
"""


def task_331_a(input_data):
    """
    There is natural number n. Is it possible to represent it as a sum of tree squared natural numbers?
    If it`s possible, return the triplet of natural numbers x, y, z, where n = x^2 + y^2 + z^2 .
    """
    if isinstance(input_data, int):
        if input_data > 0:

            for x_arg in range(input_data + 1):
                for y_arg in range(input_data + 1):
                    for z_arg in range(input_data + 1):
                        if x_arg ** 2 + y_arg ** 2 + z_arg ** 2 == input_data:
                            return [x_arg, y_arg, z_arg]

            print('There is no x, y, z')

        else:
            print('n must be bigger than 0')

    else:
        raise Exception('Type integer')


def task_331_a_menu():
    print('-' * 100)
    print(f'Function logic:\n{task_331_a.__doc__}')
    print('-' * 50)
    print("Input some integer number:\n")
    try:
        input_data = int(input())
        print(f'Result: {task_331_a(input_data)}')
    except Exception as error:
        print(f'{error}. Try again!'.title())


if __name__ == '__main__':
    task_331_a_menu()
