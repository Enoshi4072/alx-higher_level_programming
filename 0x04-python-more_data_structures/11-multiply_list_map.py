#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_l = my_list
    new_l2 = list(map(lambda x: x * number, new_l))
    return new_l2
