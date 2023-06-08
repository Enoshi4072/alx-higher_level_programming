#!/usr/bin/python3
import sys
argums = sys.argv[1:]
n_argums = len(argums)
if n_argums == 0:
    print("0 arguments.")
if n_argums == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(n_argums))
    for i, argum in enumerate(argums, 1):
        print("{}: {}".format(i, argum))
