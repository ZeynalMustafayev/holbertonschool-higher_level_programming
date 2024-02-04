#!/usr/bin/python3
"""
    The ``4. Text indentation`` module
    This module contains text_indentation function.
"""


def text_indentation(text):
    """
        text_indentation - seperate text.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text_list = []
    single_sentence = ""
    for letter in text:
        single_sentence += letter
        if letter == "." or letter == "?" or letter == ":":
            text_list.append(single_sentence)
            single_sentence = ""
    text_list.append(single_sentence)
    edited_list = []
    for txt in text_list:
        txt = txt.strip()
        edited_list.append(txt)
    output = "\n\n".join(edited_list)
    print(output, end="")
