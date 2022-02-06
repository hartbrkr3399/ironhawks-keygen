'''
IronHawks-KeyGen Example v0.1

An example file to showcase keygen.py functionality with a nice output 
delay.

Created by Praveen K. Contact: hartbrkrlegacy@gmail.com
'''


import sys
import time

import keygen


STRATEGIES = {
    1 : "Generate using Alphabets only.",
    2 : "Generate using Digits only.",
    3 : "Generate using Alphabets and Digits only.",
    4 : "Generate using Alphabets and Special Characters only.",
    5 : "Generate using Digits and Special Characters only.",
    6 : "Generate using Alphabets, Digits and Special Characters."
}


def show_strategies():
    print("Choose one of the following options to generate a password:")
    for i in range(1,7):
        print(str(i) + ". " + STRATEGIES[i])
    print("0. Exit.")


def get_strategy():
    try:
        choice = int(input("Enter the corresponding option's number(0-6): "))
        if choice < 0 or choice > 6:
            raise ValueError()
        if choice == 0:
            sys.exit("Exited.")
        return choice
    except ValueError:
        print("Invalid input! Enter a number between 0 to 6.")
        return get_strategy()
    

def get_length():
    try:
        length = int(input("Enter the preferred length of the password: "))
        if length == 0:
            sys.exit("Exited.")
        if length < 8 or length > 128:
            raise ValueError()
        return length
    except ValueError:
        print("Invalid input! Enter a number between 8 to 128 or 0 to exit.")
        return get_length()


if __name__ == '__main__':
    print(__doc__)
    show_strategies()
    strategy_number = get_strategy()

    print('''Accepted. In the following prompt, enter the preferred length of 
the password. Minimum is 8 and Maximum is 128. Recommended length is 12 to 
15 characters.''')
    password_length = get_length()

    print('''Accepted. Generating a password with strategy: '{}' and 
length: {}...'''.format(
    str(STRATEGIES[strategy_number]), str(password_length)))

    generated_password = keygen.generate(strategy_number, password_length)
    
    time.sleep(2)
    print("Password generation successful!")
    print("\nGenerated Password: {}".format(generated_password))
    time.sleep(1)
    print("\nExited.")