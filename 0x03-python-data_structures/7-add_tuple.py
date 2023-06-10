#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup_a = tuple_a[:2] + (0, 0)
    tup_b = tuple_b[:2] + (0, 0)
    ans_1 = tup_a[0] + tup_b[0]
    ans_2 = tup_a[1] + tup_b[1]
    return ans_1, ans_2
