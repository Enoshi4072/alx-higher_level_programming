#!/usr/bin/python3
def no_c(my_string):
    new_string = ''.join([idx for idx in my_string if idx not in ['c', 'C']])
    return new_string
