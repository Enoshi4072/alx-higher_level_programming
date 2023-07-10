#!/usr/bin/python3

""" A class that inherits from list """
class MyList(list):
    def print_sorted(self):
        """
        prints the list in a sorted order

        """
        print(sorted(self))
