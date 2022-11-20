#!/usr/bin/python3
"""
A unittest module
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class Test(unittest.TestCase):
    """
    Tmp
    """

    def test_max_integer(self):
        self.assertEqual(max_integer([6, 8, 9]), 9)

    def test_max_integer_neg_pos(self):
        self.assertEqual(max_integer([89, -78]), 89)

    def test_max_integer_neg(self):
        self.assertEqual(max_integer([-78, -8, -1]), -1)

    def test_max_integer_oneElement(self):
        self.assertEqual(max_integer([9]), 9)

    def test_max_integer_noElement(self):
        self.assertEqual(max_integer([]), None)

    def test_max_integer_middleElement(self):
        self.assertEqual(max_integer([67, 889, 90]), 889)
