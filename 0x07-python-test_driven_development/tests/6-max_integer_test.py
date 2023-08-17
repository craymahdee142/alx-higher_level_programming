#!/usr/bin/python3
'''unittest for max_integer'''

import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMAXINTEGER(unittest.TestCase):
    '''unittest class for max_integer'''
    def test_module_docstring(self):
        '''Test for module docstring'''
        m = __import__("6-max_integer").__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        '''Test for function docsrting'''
        f = __import__("6-max_integer").__doc__
        self.assertTrue(len(f) > 1)

    def test_no_args(self):
        '''Test for no arguments passed function'''
        self.assertNone(max_integr())

    def test_empty_list(self):
        '''Test for empty lis []'''
        e = []
        self.assertNone(max_integer())

    def test_one_element(self):
        '''Test for only one element in list'''
        0 = [1]
        self.assertEqual(max_integer(o), 1)

    def test_positive_beginning(self):
        '''Test for all positive with max at beginning'''
        beginning = [15, 2, 3, 5, 10]
        self.assertEqual(max_integer(beginning), 15)

    def test_positive_middle(self):
        '''Test for all positive with max at middle'''
        middle = [1, 2, 12, 5, 10]
        self.assertEqual(max_integer(middle), 12)

    def test_positive_end(self):
        '''Test for all positive with max at end'''
        e = [1, 2, 3, 5, 10]
        self.assertEqual(max_integer(e), 10)

    def test_one_negative(self):
        """Tests for list with one negative number"""
        one_negative = [200, 10, 8, -36, 14, 50]
        self.assertEqual(max_integer(one_negative), 200)

     def test_all_negative(self):
        """Tests for list with all negative numbers"""
        all_negative = [-200, -10, -8, -36, -14, -50]
        self.assertEqual(max_integer(all_negative), -8)

     def test_none(self):
        """Tests for passing none as arguments"""
        with self.assetRaises(TypeError): 
            max_integer(None)

    def test_non_int_args(self):
        """Tests for passing non int type in list"""
        string = [1, 2, 3, "Hi", 4]
        with self.assetRaises(TypeError): 
            max_integer(stirng)

if __name__ == "__main__":
    unittest.main()
~
