"""
Task 01.
Task 88 c, d.
Given a natural number n:
     c) Rearrange the first and last digits of n.
     d) Assign one digit to the beginning and the end of the record of the number n.
"""
__author__ = 'Oleksandr Krynytskyi'

def swap_digit(digit):
    """c) Rearrange the first and last digits of n."""
    swappable = [int(x) for x in str(digit)]
    swappable[-1], swappable[0] = swappable[0], swappable[-1]
    return int(''.join(map(str, swappable)))


def write_digit(digit):
    """d) Assign one digit to the beginning and the end of the record of the number n."""
    return '1' + str(digit) + '1'

def main():
    """Main function to execute this module"""
    print(__doc__)

    while True:
        print(f"""If you want to terminate this app, please enter your input as 'q', 'quit', 'exit',
'stop' or 'terminate'""")
        user_input = input("Select your sub-tasks (1 or 2): ")
        if user_input == '1':
            print("To return to sub-task selector, please enter any input except digits")
            try:
                print(swap_digit(int(input("Enter your digit: "))))
                continue
            except ValueError:
                print("Wrong input!")
        elif user_input == '2':
            try:
                print(write_digit(int(input("Enter your digit: "))))
                continue
            except ValueError:
                print("Wrong input!")
        else:
            if user_input.lower() in ['q', 'quit', 'exit', 'stop', 'terminate']:
                quit("Exiting...")
            print("Wrong input!")
            continue
