#!/usr/bin/python3
""" Function to read a file """


def read_file(filename=""):
    """ Use with statement to read contents """

    with open(filename, 'r', encoding='UTF8') as r_file:
        """ read file contents """
        r_file_contents = r_file.read()
        """ Printing to the stdout """
        print(r_file_contents, end="")
