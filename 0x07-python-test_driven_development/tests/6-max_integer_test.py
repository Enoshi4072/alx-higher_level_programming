#!/usr/bin/python3

""" Unittest for a function that finds a max_integer in a list """

import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ The tests for the max_integer function. """
    def test_one_element(self):
        """ When the list contains a single element """
        self.assertEqual(max_integer([5]), 5)

    def test_positive_ordered_elements(self):
        """ When the list is composed of ordered positive elements """
        self.assertEqual(max_integer([10, 20, 30, 40, 50]), 50)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_ordered_elements(self):
        """ When the list is composed of negative ordered elements """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-50, -60, -70, -80]), -50)

    def test_positive_unordered_elements(self):
        """ When the list is composed of unordered positive elements """
        self.assertEqual(max_integer([5 ,40, 21, 39, 2, 35]), 40)
        self.assertEqual(max_integer([3,1,8,3,5,4]), 8)

    def test_negative_unordered_elements(self):
        """ When the list is composed of unordered negative elements """
        self.assertEqual(max_integer([-5, -8,-1, -3, -2]), -1)

    def test_combined_positive_and_negative(self):
        """ When the list is composed of both posive and negative elements """
        self.assertEqual(max_integer([-4, 7, 0, -3, 6, -9]), 7)

    def test_positive_floats(self):
        """ When the list is composed of floats """
        self.assertEqual(max_integer([4.3, 2.5, 3.4, 8.7]), 8.7)

    def test_negative_floats(self):
        """ When the list id composed of negative floats """
        self.assertEqual(max_integer([-2.3, -0.9, -3.1, -3.2]), -0.9)

    def test_combined_ints_floats(self):
        """ When the list is composed of both ints and floats """
        self.assertEqual(max_integer([4.5, 2.7, -7.8, -110, 43]), 43)

    def test_empty_list(self):
        """ When the list is empty """
        self.assertIsNone(max_integer([]))

    def test_dup_elem(self):
        """ When the elements """
        self.assertEqual(max_integer([2, 2, 5, 1, 5, 1]), 5)

    def test_single_string(self):
        """ When a string is provided as a list """
        self.assertEqual(max_integer(["Javascript"]), "Javascript")

    def test_multiple_strings(self):
        """ When multiple strings are provided """
        self.assertEqual(max_integer(["I", "will", "One", "day", "be", "a", "pro"]), "will")

    def test_strings_ints_floats(self):
        """ When integers, numbers """
        self.assertEqual(max_integer(["Juma", "Is", "26", "Mary", "21"]), "Mary")

if __name__ == '__main__':
    unittest.main()
