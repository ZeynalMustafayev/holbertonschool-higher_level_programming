#!/usr/bin/python3
"""My integer"""


class MyInt(int):
    """Class is documented"""
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
