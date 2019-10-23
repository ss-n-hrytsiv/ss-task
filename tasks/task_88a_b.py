__author__ = 'Marta Kozak'

def is_3_in_nn(number):
    '''find out whether '3' is in a number's square'''

    if not isinstance(number, int):
        raise ValueError("Please enter the number")

    for digit in range(len(str(number**2))):
        if str(number**2)[digit]=='3':
            return True
    return False


def reverse_number(number):
    '''change the order of digits to the opposite'''

    if not isinstance(number, int):
        raise ValueError("Please enter the number")
    
    reversed_num=0
    while number>0:
        reversed_num=reversed_num*10+number%10
        number=number//10
    return reversed_num

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
            if user_choice=='a':
                print(user_input, "has a '3' in it's square: ", is_3_in_nn(user_input))
            elif user_choice=='b':
                print("Reversing ", user_input, "... Result: ", reverse_number(user_input))

        except ValueError:
            if user_input.lower() in ['q', 'quit', 'exit', 'stop', 'terminate']:
                break
            print('n - must be an int type!')
            continue


def task88_a_b_menu():
    
    while True:
        chosen_task = input('Select sub-task - [a / b]: ')
    
        if chosen_task.lower() == 'a':
            represent_function(is_3_in_nn, is_3_in_nn.__doc__, 'a')
        elif chosen_task.lower() == 'b':
            represent_function(reverse_number, reverse_number.__doc__, 'b')
        elif chosen_task.lower() in ['q', 'quit', 'exit', 'stop', 'terminate']:
            break
        else:
            print('You can only choose: [a / b]')
            continue


if __name__ == '__task88_a_b_menu__':
    task88_a_b_menu()


