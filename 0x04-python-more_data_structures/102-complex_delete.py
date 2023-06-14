#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_del = []
    for i, j in a_dictionary.items():
        if j == value:
            to_del.append(i)
    for i in to_del:
        del a_dictionary[i]
    return a_dictionary
