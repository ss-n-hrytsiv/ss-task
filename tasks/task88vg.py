"""
Task 01.
Задание 88 в, г.
Дано натуральное число n:
    в) Переставить первую и последнюю цифры числа n.
    г) Приписать по единице в начало и в конец записи числа n.
"""


def write_digit(digit):
    """г) Приписать по единице в начало и в конец записи числа n."""
    return '1' + str(digit) + '1'


def main():
    """Main function to execute this module"""
    print(__doc__)

    while True:
        print("To return to the main app enter any key except 1 or 2")
        user_input = input("Select your sub-tasks (1 or 2): ")
        if user_input == '1':
            try:
                digit = int(input("Enter your digit: "))
                swappable = [int(x) for x in str(digit)]
                swappable[-1], swappable[0] = swappable[0], swappable[-1]
                return (int(''.join(map(str, swappable))))
            except ValueError:
                print("Wrong input!")
        elif user_input == '2':
            try:
                return (write_digit(int(input("Enter your digit: "))))
            except ValueError:
                print("Wrong input!")
        else:
            break
