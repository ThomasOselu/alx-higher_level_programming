#!/usr/bin/python3
"""defining a text indentation"""


def text_indentation(text):
    """prints text indentation with 2 new lines
    args:
        text: a text to be printed
    raises:
        TypeError("text must be a string")
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    for char in text:
        if char in [".", "?", ":"]:
            print(f'{char}\n')
            continue
        print(char, end="")
