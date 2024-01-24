#!/usr/bin/python3
def print_last_digit(number):
    if (number > 0):
        number1 = number % 10
    else:
         number1 = -1 * number % 10
    print("{}".format(number1), end="")
    return (number1)
