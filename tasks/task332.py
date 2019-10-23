"""
Task 02.
Task 332.
It is known that any natural number can be represented in the form of a sum of
no more than four squares of natural numbers or, what is the same, in the form
of a sum of four squares of non-negative integers (Lagrange's theorem).
Given a natural n; indicate such non-negative x, y, z, t , where n = x^2 + y^2 + z^2 + t^2 .
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
