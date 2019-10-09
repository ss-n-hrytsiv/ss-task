# 226
# Дано натуральні n, m. Отримати всі їх натуральні спільні кратні, менші mn


def task_226():
    print('Введіть натуральні N i M, щоб отримати всі їх натуральні спільні кратні, менші mn.')

    while True:
        n = input('Введіть натуральне N:\n')
        if not n.isdigit():
            print('Схоже Ви ввели не число...')
            continue
        elif n == 0:
            print('0 не є натуральним числом!')
            continue
        else:
            n = int(n)
            while True:
                m = input('Введіть натуральне M:\n')
                if not m.isdigit():
                    print('Схоже Ви ввели не число...')
                    continue
                elif m == 0:
                    print('0 не є натуральним числом!')
                    continue
                else:
                    m = int(m)
                    break
            break
    seq = [n, m]
    n, m = seq[0], seq[1]
    mn = m * n
    s_k_n = [i for i in range(1, mn + 1) if i % n == 0]
    s_k_m = [i for i in range(1, mn + 1) if i % m == 0]

    s_k = sorted(list(set(s_k_n) & set(s_k_m)))

    return s_k_n, s_k_m, s_k
