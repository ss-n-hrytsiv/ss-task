__author__ = 'Nazar Hrytsiv'


def task_86_a(n):
    """Task 86_a: Have a natural number n how many digits in this number n"""
    if type(n) != int:
        raise TypeError('Argument must be an integer type!')
    n = str(n)
    answer = len(list(n))
    return answer


def task_86_b(n):
    '''Task 86_b: Have a natural number n count the sum of all digits in number n'''
    if type(n) != int:
        raise TypeError('Argument must be an integer type!')
    n = str(n)
    return sum(map(int, n))


def represent_function(function, function_doc, user_choice):
    while True:
        print('*' * 100)
        print('Function logic: ' + '\n' + function_doc)
        print('-' * 50)
        print('Input only number')
        print('If you want to exit, just input smth from: q /quit / exit /stop /terminate')
        print('-' * 50)

        user_input = input('Please input a number: ')

        try:
            user_input = int(user_input)
            if user_choice == 'a':
                print(user_input, "Count of digits in number is: ", task_86_a(user_input))
            elif user_choice == 'b':
                print("Sum of all digits in number ", user_input, "... Result: ", task_86_b(user_input))

        except ValueError:
            if user_input.lower() in ['q', 'quit', 'exit', 'stop', 'terminate']:
                break
            print('n - must be an int type!')
            continue


def task86_a_b_menu():
    while True:
        chosen_task = input('Select sub-task - [a / b]: ')

        if chosen_task.lower() == 'a':
            represent_function(task_86_a, task_86_a.__doc__, 'a')
        elif chosen_task.lower() == 'b':
            represent_function(task_86_b, task_86_b.__doc__, 'b')
        elif chosen_task.lower() in ['q', 'quit', 'exit', 'stop', 'terminate']:
            break
        else:
            print('You can only choose: [a / b]')
            continue


