#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = number * -1

l_num = number % 10
message = "Last digit of {} is {} ".format(number, l_num)

if l_num > 5:
    message += " and is greater than 5"
elif l_num == 0:
    message += " and is 0"
else:
    message += "and is less than 6 and not 0"

print(message)
