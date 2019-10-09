#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
554
Дано натуральное число n. Получить все пифагоровы
тройки натуральних чисел, каждое из которых превосходит n, т. е.
все такие тройки натуральных чисел a, b, c, что:
    a^2 + b^2 = c^2     (a <= b <= c <= n)
'''
__author__ = 'Stanislav Hrytcyshyn'

from itertools import product


def find_all_pythagorean_triple(n):
    '''
    returns all pythagorean triple 
    which satisfies an equation:
    a^2 + b^2 = c^2     (a <= b <= c <= n)
    '''
    if type(n) != int:
        raise TypeError('Argument must be an integer type!')
    
    result = []

    combinations = [comb for comb in product(range(n + 1), repeat=3)]

    for comb in combinations:
        a, b, c = comb
        if a ** 2 + b ** 2 == c ** 2:
            result.append(comb)

    return result


def task554_menu():
    while True:
        print('-' * 100)
        print('Function logic: ' + '\n' + find_all_pythagorean_triple.__doc__)
        print('-' * 50)
        print('Input only number')
        print('If you wnat to exit, just input smth from: q /quit / exit /stop /terminate')
        print('-' * 50)

        user_input = input('Please input a number: ')

        try:
            user_input = int(user_input)

            print('All pythagorean triplets: ')
            for triplet in find_all_pythagorean_triple(n=user_input):
                print(triplet, '\n')

        except ValueError:
            if user_input.lower() in ['q', 'quit', 'exit', 'stop', 'terminate']:
                break
            print('n - must be an int type!')
            continue


if __name__ == '__main__':
    task554_menu()
        





