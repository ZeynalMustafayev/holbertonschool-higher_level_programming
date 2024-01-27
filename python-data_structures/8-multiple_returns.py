#!/usr/bin/python3
def multiple_returns(sentence):
    len_string = len(sentence)
    if (len_string > 0):
        i = sentence[0]
    else:
        i = None
    return (len_string, i)
