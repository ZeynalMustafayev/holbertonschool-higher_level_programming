#!/usr/bin/python3
"""function that prints a text with 2 new lines after each of /
these characters: ., ? and :"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines after each /
    of these characters: ., ? and :
    unit tests located in tests/5-text_indentation.txt
    checks for type errors
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    elements = [".", "?", ":"]
    lines = []
    current_line = ""

    for char in text:
        current_line += char
        if char in elements:
            lines.append(current_line.strip())
            current_line = ""

    if current_line:
        lines.append(current_line.strip())

    print('\n'.join(lines))
