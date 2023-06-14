#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    big_key = None
    big_val = 0
    for i, j in a_dictionary.items():
        if j > big_val:
            big_key = i
            big_val = j
    return big_key
