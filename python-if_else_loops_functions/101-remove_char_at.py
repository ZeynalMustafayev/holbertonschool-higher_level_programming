#!/usr/bin/env python3
def remove_char_at(str, n):
    if n < 0:
        return str
    a = str[:n] + str[n + 1:]
    return a
