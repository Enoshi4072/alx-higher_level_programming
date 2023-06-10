#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        """newlist = my_list.copy()"""
        newlist = [i for i in my_list]
        if idx < 0:
            return newlist
        length = len(my_list) - 1
        if idx > length:
            return newlist
        newlist[idx] = element
        return newlist
