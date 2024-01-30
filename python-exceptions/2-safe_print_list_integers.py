#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    value_count = 0
    try:
        for i in range(x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                value_count += 1
    except (ValueError, IndexError):
        return (IndexError)
    print()
    return value_count
