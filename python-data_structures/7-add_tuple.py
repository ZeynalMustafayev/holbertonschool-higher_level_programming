#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_o = (0, )
    for i in range(len(tuple_a), 2):
        tuple_a += tuple_o
    for i in range(len(tuple_b), 2):
        tuple_b += tuple_o
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple
