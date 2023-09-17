#!/usr/bin/python3
"""test cases for project"""


import unittest
from models.base import Base
from models.square import Square
import json
import inspect

class test_base(unittest.Testcase):
    """class for test cases"""

    def test_no_id(self):
        """no id"""
        b = Base()
        self.assertEqual(1, b.id)

    def test_valid_id(self):
        """valid id"""
        b = Base()
        self.assertEqual(50, b.id)

    def test_zero_id(self):
        """zero id"""
        b = Base()
        self.assertEqual(0, b.id)

