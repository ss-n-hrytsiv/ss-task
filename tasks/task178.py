#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
178
Даны натуральные числа n, a_1, ..., a_n.
Определить количество членов a_k последовательности a_1, ..., a_n:

б) Кратных 3 и не кратных 5
в) являющихся квадратами четных чисел
'''

__author__ = 'Stanislav Hrytcyshyn'

import math


def find_multiples(input_list):
    '''
        returns a count of numbers
        which are multiple of 3 but
        aren't multiple of 5
    '''
    try:
        argument = iter(input_list)
    except TypeError:
        return 'Argument should be an iterable object'

    return len(list(filter(lambda x: x % 3 == 0 and x % 5 != 0, input_list)))


def find_squares_of_even_numbers(input_list):
    '''
        returns a count of numbers
        which are squares of even numbers
    '''
    print(input_list)
    try:
        argument = iter(input_list)
    except TypeError:
        return 'Argument should be an iterable object'

    return len(list(filter(lambda x: math.sqrt(x) % 2 == 0, input_list)))


def represent_function(function, function_doc, resulted_text):
    print('-' * 100)
    print('Function logic: ' + '\n' + function_doc)
    print('-' * 50)
    print('Input only numbers')
    print('If you want to stop press #Enter# again!')
    print('If you wnat to stop, just input smth from: q /quit / exit /stop /terminate')
    print('-' * 50)
        
    user_list = []

    while True:
            
        user_input = input('Next number: ')

        if user_input == '':
            print(f'{resulted_text}', function(user_list))
            break

        try:
            next_element = int(user_input)
            user_list.append(next_element)
        except ValueError:
            print('Please, input only numbers')
            continue


def task178_menu():

    while True:
        chosen_task = input('Select sub-task - [b / c]: ')
    
        if chosen_task.lower() == 'b':
            represent_function(find_multiples, find_multiples.__doc__, 'Count of numbers which are multiple of 3 but arent multiple of 5: ')
        elif chosen_task.lower() == 'c':
            represent_function(find_squares_of_even_numbers, find_squares_of_even_numbers.__doc__, 'Count of numbers which are squares of even numbers: ')
        elif chosen_task.lower() in ['q', 'quit', 'exit', 'stop', 'terminate']:
            break
        else:
            print('You can only choose: [b / c]')
            continue


if __name__ == '__task178_menu__':
    task178_menu()