#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = number * -1

l_num = number % 10
message = "Last digit of "

if l_num > 5:
    print(f"Last digit of {number} is {l_num} and is greater than 5")
elif l_num == 0:
    print(f"Last digit of {number} is {l_num} and is 0")
else:
    print(f"Last digit of {number} is {l_num} and is less than 6 and not 0")
