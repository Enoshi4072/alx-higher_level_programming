#!/usr/bin/python3
""" Writes to a text file """


def write_file(filename="", text=""):
    """ Utilizes a with statement to handle close """

    with open(filename, 'w', encoding='UTF8') as r_file:
        """ Writing to the file """
        r_file.write(text)
        """ Getting the number of characters """
        position = r_file.tell()
        return position
