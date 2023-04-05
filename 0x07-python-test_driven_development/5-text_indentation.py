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
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
