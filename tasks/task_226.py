# 226
# Дано натуральні n, m. Отримати всі їх натуральні спільні кратні, менші mn


def task_226(n, m):
    """Дано натуральні n, m. Отримати всі їх натуральні спільні кратні, менші mn."""

    mn = m * n
    s_k_n = [i for i in range(1, mn + 1) if i % n == 0]
    s_k_m = [i for i in range(1, mn + 1) if i % m == 0]

    s_k = sorted(list(set(s_k_n) & set(s_k_m)))

    return s_k


def task_226_menu():
    while True:
        print('-' * 100)
        print('Function logic: ' + '\n' + task_226.__doc__)
        print('-' * 50)
        print('-' * 100)
        print('Input only number')
        print('If you wnat to exit, just input smth from: q /quit / exit /stop /terminate')
        print('-' * 50)
        print('\n\n\n')
        user_input_n = input('Please input a first number(n): ')
        if user_input_n.lower() in ['q', 'quit', 'exit', 'stop', 'terminate']:
            break
        user_input_m = input('Please input a second number(m): ')

        try:

            n = int(user_input_n)
            m = int(user_input_m)
            s_k = task_226(n, m)
            print(f'Спільні кратні для {n} i {m}, менші за {m*n} = {s_k}')
            print('\n\n\n')
        except ValueError:
            # if user_input_n.lower() in ['q', 'quit', 'exit', 'stop', 'terminate']:
            #     break
            print('n - must be an int type!')
            continue


if __name__ == "__main__":
    task_226_menu()
