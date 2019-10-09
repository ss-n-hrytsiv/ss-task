"""
python 3.7
author: Andrew Stanishevskyi
"""


def task_108():
    """
    Дано натуральное число n. Получить наименьшее число
    вида 2^r , превосходящее n.
    """
    input_data = input("Enter n: ")
    try:
        input_data = int(input_data)
        if input_data > 0:
            for i in range(input_data + 1):
                two_to_i_power = 2 ** i
                if two_to_i_power > input_data:
                    return two_to_i_power
        else:
            return 'n must be bigger than 0'
    except ValueError:
        return 'Type integer'
