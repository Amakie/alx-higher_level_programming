#!/usr/bin/python3

"""unitest for function max_integer"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer"""

    def test_empty_list(self):
        """checks if list is empty"""
        empty = []
        self.assertEqual(max_integer(empty), [])

    def test_right_order(self):
        """checks for the order of the integers"""
        right_order = [1, 2, 3, 4]
        self.assertEqual(max_integer(right_order), 4)

    def test_wrong_order(self):
        """when the list is not properly ordered"""
        wrong_order = [1, 3, 4, 2]
        self.assertEqual(max_integer(wrong_order), 4)

    def test_highest_first(self):
        """test for list with the higheest number first"""
        highest_first = [4, 3, 2, 1]
        self.assertEqual(max_integer(highest_first), 4)

    def test_floats(self):
        """test for list with floats"""
        floats = [1.3, 6.7, 18.7, 2.3]
        self.assertEqual(max_integer(floats), 18.7)

    def test_strings(self):
        """test for strings"""
        strings = "today"
        self.assertEqual(max_integer(strings), y)

    def test_strings_list(self):
        """test for list of strings"""
        string_list = ["Today" "is" "a" "great" "day"]
        self.assertEqual(max_integer(string_list), day)

    def test_empty_string(self):
        """test for empty string"""
        empty_string = ""
        self.assertEqual(max_integer(empty_string), None)


    def test_mix_int_float(self):
        """test for a mix of integer and floats"""
        mix = [2, 3.5, 10.0, 14.5]
        self.assertEqual(max_integer(mix), 14.5)

    def test_one_element(self):
        """test for one element"""
        one_element = [9]
        self.assertEqual(max_integer(one_element), 9)

if __name__ = '__main__':
    unittest.main()


