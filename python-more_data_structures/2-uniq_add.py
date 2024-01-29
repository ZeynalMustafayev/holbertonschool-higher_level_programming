#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set()
    result = 0
    for i in my_list:
        if i not in unique_set:
            unique_set.add(i)
            result += i
    return (result)
