#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base('b')
    print(b1.id)

    b2 = Base(14)
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(-12)
    print(b4.id)

    b5 = Base(1)
    print(b5.id)
