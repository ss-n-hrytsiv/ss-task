# 559
# Дано натуральне n. Знайти всі, менші n числа Мерсенна.
import math


def task_559():
    n = input("Enter n: ")
    num_mers = [(2 ** i - 1) for i in range(1, n + 1)]
    simple_num = []

    # for i in range(1, n+1):
    #     num_mers.append(2 ** i - 1)

    for count in range(2, n+1):
        i = 2
        limit = int(math.sqrt(count))
        while i <= limit:
            if count % i == 0:
                break
            i += 1
        else:
            simple_num.append(count)
    simple_num_mers = [(2 ** i + 1) for i in simple_num]
    # for i in simple_num:
    #     simple_num_mers.append(2 ** i - 1)

    return num_mers, simple_num_mers
