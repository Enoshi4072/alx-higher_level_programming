#!/usr/bin/python3
""" function that appends a string at the end of a text file """


def append_write(filename="", text=""):
    """ Use with to handle close """

    with open(filename, 'a', encoding='UTF8') as r_file:
        """ Writing to the file """
        r_file.write(text)
        """ Return the number of characters """
        return len(text)
