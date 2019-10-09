"""
python 3.7
author: Andrew Stanishevskyi
"""


def task_331_b():
    """
    Дано натуральное число n. Можно ли представить его в
    виде суммы трех квадратов натуральных чисел? Если можно, то
    указать все тройки x, y, z таких натуральных чисел, что
    n = x^2 + y^2 + z^2 .
    """
    input_data = input("Enter n: ")

    try:
        input_data = int(input_data)

        if input_data > 0:

            output = []
            for x_arg in range(input_data + 1):
                for y_arg in range(input_data + 1):
                    for z_arg in range(input_data + 1):
                        if x_arg ** 2 + y_arg ** 2 + z_arg ** 2 == input_data:
                            output.append([x_arg, y_arg, z_arg])

            return output
        else:
            return 'n must be bigger than 0'
    except ValueError:
        return 'Type integer'
