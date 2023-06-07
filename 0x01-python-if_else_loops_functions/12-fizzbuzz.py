#!/usr/bin/python3
def fizzbuzz():
    f = "Fizz"
    b = "Buzz"
    fb = "FizzBuzz"
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            print("{} ".format(fb), end='')
        elif i % 3 == 0:
            print("{} ".format(f), end='')
        elif i % 5 == 0:
            print("{} ".format(b), end='')
        else:
            print("{} ".format(i), end='')
