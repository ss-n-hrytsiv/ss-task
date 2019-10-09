"""
Task 02.
Задание 332.
Известно, что любое натуральное число можно представить
в виде суммы не более чем четырех квадратов натуральных чисел или,
что то же самое, в виде суммы четырех квадратов неотрицательных
целых чисел (теорема Лагранжа). Дано натуральное n; указать такие
неотрицательные x, y, z, t , что n = x^2 + y^2 + z^2 + t^2 .
"""


def lagrange(digit):
    """Lagrange's four-square theorem"""
    result = []
    for _ in range(4):
        _ = int(digit ** 0.5)
        digit = digit - _ ** 2
        result.append(_)
    return result


def task332_menu():
    """Main function to execute this module"""
    print(__doc__)
    try:
        user_input = int(input("Enter your digit: "))
        return lagrange(user_input)
    except ValueError:
        print("Wrong input!")


# if __name__ == '__task332_menu__':
#     task332_menu()