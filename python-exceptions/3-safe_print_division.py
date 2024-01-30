#!/usr/bin/python3
def safe_print_division(a, b):
    c = None
    try:
        c = a/b
        return c
        #print("{}".format(c))
    except ZeroDivisionError:
        print(None)
    finally:
        print("Inside result: {}".format(c))
