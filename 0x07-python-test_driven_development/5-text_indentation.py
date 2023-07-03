#!/usr/bin/python3

def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The strings to be indented

    Raises:
        TypeError: If the text provided is not a string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        print(char, end='')

        if char in ['.', '?', ':']:
            print("\n\n", end='')
