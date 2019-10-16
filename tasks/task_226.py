# 226
# Дано натуральні n, m. Отримати всі їх натуральні спільні кратні, менші mn
__author__ = 'Orest Furda'

def task_226(n, m):
    """Дано натуральні n, m. Отримати всі їх натуральні спільні кратні, менші mn."""
    # print('Введіть натуральні N i M, щоб отримати всі їх натуральні спільні кратні, менші mn.')

    # while True:
    #     n = input('Введіть натуральне N:\n')
    #     if not n.isdigit():
    #         print('Схоже Ви ввели не число...')
    #         continue
    #     elif n == 0:
    #         print('0 не є натуральним числом!')
    #         continue
    #     else:
    #         n = int(n)
    #         while True:
    #             m = input('Введіть натуральне M:\n')
    #             if not m.isdigit():
    #                 print('Схоже Ви ввели не число...')
    #                 continue
    #             elif m == 0:
    #                 print('0 не є натуральним числом!')
    #                 continue
    #             else:
    #                 m = int(m)
    #                 break
    #         break

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
