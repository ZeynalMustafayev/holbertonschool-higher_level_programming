#!/usr/bin/python3
def multiple_returns(sentence):
    len_string = len(sentence)
    i = sentence[0]
    new_tuple = (len_string, i)
    if new_tuple:
        return (new_tuple)
    else:
        return (None)
