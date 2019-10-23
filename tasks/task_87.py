# 87
# Given are natural n, m. Obtain the sum m of the last digits of the number n.
__author__ = 'Orest Furda'

def task_87(number, number_of_digits):
    """Given are natural n, m. Obtain the sum m of the last digits of the number n."""
    result = sum(number[-number_of_digits:])

    return result


def task_87_menu():
    while True:
        print('-' * 100)
        print('Function logic: ' + '\n' + task_87.__doc__)
        print('-' * 50)
        print('-' * 100)
        print('Input only number')
        print('If you wnat to exit, just input smth from: q /quit / exit /stop /terminate')
        print('-' * 50)
        print('\n\n\n')

        user_input_number = input('Please input a first number(n): ')

        if user_input_number.lower() in ['q', 'quit', 'exit', 'stop', 'terminate']:
            break

        user_input_number_of_digits = input('Please input a second number(m): ')

        try:
            number = list(map(int, user_input_number))
            number_of_digits = int(user_input_number_of_digits)
            print(f"Sum m of the last digits of the number n = {task_87(number, number_of_digits)}")
            print('\n\n\n')
        except ValueError:
            print('n - must be an int type!')
            continue


if __name__ == "__main__":
    task_87_menu()
