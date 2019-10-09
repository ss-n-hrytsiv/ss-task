# 87
# Дано натуральні n, m. Отримати суму m останніх цифр числа n.


def task_87():
    print('Введіть натуральні N i M, щоб отримати суму m останніх цифр числа n.')
    while True:
        n = input('Введіть натуральне N:\n')
        if not n.isdigit():
            print('Схоже Ви ввели не число...')
            continue
        elif n == 0:
            print('0 не є натуральним числом!')
            continue
        else:
            n = list(map(int, n))
            while True:
                m = input('Введіть натуральне M:\n')
                if not m.isdigit():
                    print('Схоже Ви ввели не число...')
                    continue
                elif m == 0:
                    print('0 не є натуральним числом!')
                    continue
                elif int(m) > len(n):
                    print(
                        f'Вибачте, але у максимальне значення для M може бути {len(n)}')
                    continue
                else:
                    m = int(m)
                    break
            break
    seq = [n, m]
    print(seq)
    n, m = seq[0], seq[1]
    result = sum(n[-m:])

    return result
