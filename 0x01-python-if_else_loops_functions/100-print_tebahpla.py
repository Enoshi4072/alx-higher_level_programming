#!/usr/bin/python3
i = 0
for i, c in enumerate(range(122, 96, -1)):
    value = 32 if i % 2 == 0 else 0
    print("{:c}".format(value), end="")
