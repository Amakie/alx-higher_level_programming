#!/usr/bin/python3
import unittest
from models.base import Base
from models.base import Square
import json
import inspect

"""test cases for base module"""

class test_base(unittest.TestCase):
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

    def test_string_id(self):
        """string id"""
        b = Base("Today")
        self.assertEqual("Today", b.id)

    def test_negative_id(self):
        """negative id"""
        b = Base(-50)
        self.assertEqual(-50, b.id)

    def test_list_id(self):
        """list id"""
        b = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], b.id)

    def test_dict_id(self):
        """dictionary id"""
        b = Base({"id": 100})
        self.assertEqual({"id": 100}, b.id) 

    def test_tupple_id(self):
        """tupple id"""
        b = Base(8,)
        self.assertEqual((8,), b.id)

    def test_jsontype(self):
        """test json type"""
        sq = Square(1)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_to_json_value(self):
        '''
            Testing the json string
        '''
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string),
                         [{"id": 609, "y": 0, "size": 1, "x": 0}])

    def test_to_json_None(self):
        """Testing the json string"""
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_Empty(self):
        """Testing the json string"""
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

class TestSquare(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """new class method for docstrings"""
        cls.setUp = inspect.getmembers(Base, inspect.isfunction)

    def test_docstrings(self):
        """checks if docstrings exists"""
        self.assertTrue(len(Base.__doc__) >= 1)

    
