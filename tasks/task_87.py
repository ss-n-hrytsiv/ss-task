# 87
# Дано натуральні n, m. Отримати суму m останніх цифр числа n.


def task_87(n, m):
    """Дано натуральні n, m. Отримати суму m останніх цифр числа n."""
    result = sum(n[-m:])

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
        user_input_n = input('Please input a first number(n): ')
        if user_input_n.lower() in ['q', 'quit', 'exit', 'stop', 'terminate']:
            break
        user_input_m = input('Please input a second number(m): ')

        try:
            n = list(map(int, user_input_n))
            m = int(user_input_m)
            print(task_87(n, m))
        except ValueError:
            # if user_input_n.lower() in ['q', 'quit', 'exit', 'stop', 'terminate']:
            #     break
            print('n - must be an int type!')
            continue


if __name__ == "__main__":
    task_87_menu()
