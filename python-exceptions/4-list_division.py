#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            element_1 = my_list_1[i]
            element_2 = my_list_2[i]
            result = element_1 / element_2
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except (TypeError, ValueError):
            print("wrong type")
            result = 0
        except (IndexError):
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list
