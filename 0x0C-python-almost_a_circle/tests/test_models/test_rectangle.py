#!/usr/bin/python3
from contextlib import redirect_stdout
import inspect
import io
import unittest
from models.base import Base
from models.rectangle import Rectangle
import json



class test_rectangle(unittest.TestCase):
    """Testing rectangle"""

    def setUp(self):
        self.r = Rectangle(5, 10)

    def tearDown(self):
        del self.r

    def test_width(self):
        self.assertEqual(5, self.r.width)

    def test_height(self):
        self.assertEqual(10, self.r.height)

    def test_x(self):
        self.r.x = 54
        self.assertEqual(54, self.r.x)
        self.assertEqual(0, self.r.y)

    def test_y(self):
      
        self.r.y = 45
        self.assertEqual(45, self.r.y)
        self.assertEqual(0, self.r.x)

    def test_arectangle_id(self):
       
        rect = Rectangle(1, 3, 0, 0, 199)
        self.assertEqual(199, rect.id)

    def test_width_string(self):
        
        with self.assertRaises(TypeError):
            rect = Rectangle("1", 5)

    def test_width_bool(self):
        
        with self.assertRaises(TypeError):
            rect = Rectangle(True, 5)

    def test_width_list(self):
       
        with self.assertRaises(TypeError):
            rect = Rectangle([10, 6], 5)

    def test_height_string(self):
       
        with self.assertRaises(TypeError):
            rect = Rectangle(1, "5")

    
    def test_height_list(self):
        
        with self.assertRaises(TypeError):
            rect = Rectangle(5, [10, 6])

    def test_x_string(self):
      
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, "46")

    