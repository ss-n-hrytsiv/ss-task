"""
Task 02.
Задание 332.
Известно, что любое натуральное число можно представить
в виде суммы не более чем четырех квадратов натуральных чисел или,
что то же самое, в виде суммы четырех квадратов неотрицательных
целых чисел (теорема Лагранжа). Дано натуральное n; указать такие
неотрицательные x, y, z, t , что n = x^2 + y^2 + z^2 + t^2 .
"""
__author__ = 'Oleksandr Krynytskyi'


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
    print(f"""If you want to terminate this app, please enter your input as 'q', 'quit', 'exit',
'stop' or 'terminate'""")
    while True:
        user_input = input("Enter your digit: ")
        try:
            print(lagrange(int(user_input)))
            continue
        except ValueError:
            if user_input.lower() in ['q', 'quit', 'exit', 'stop', 'terminate']:
                quit("Exiting...")
            print("Wrong input!")
            continue
