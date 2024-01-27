#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    iflen( my_list) == 0 or idx < 0 or idx >= len(my_list):
        return (my_list)
    if idx < len(my_list):
        del my_list[idx]
    return (my_list)
