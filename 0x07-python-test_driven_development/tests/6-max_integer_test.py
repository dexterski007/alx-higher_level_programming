#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unittest for max intgeer module"""
    def test_void(self):
        """test for max int"""
        self.assertEqual(max_integer(), None)

    def test_empty(self):
        """test for max int"""
        self.assertEqual(max_integer([]), None)

    def test_int(self):
        """test for max int"""
        self.assertEqual(max_integer([5]), 5)

    def test_same(self):
        """test for max int"""
        self.assertEqual(max_integer([10, 10, 10, 10]), 10)

    def test_order(self):
        """test for max int"""
        self.assertEqual(max_integer([1, 10, 20, 55]), 55)

    def test_revorder(self):
        """test for max int"""
        self.assertEqual(max_integer([99, 55, 20, 10]), 99)

    def test_unorder(self):
        """test for max int"""
        self.assertEqual(max_integer([99, 55, 155, 10]), 155)

    def test_unorderl(self):
        """test for max int"""
        self.assertEqual(max_integer([99, 55, 21, 54, 55, 155, 10]), 155)

    def test_unorder2(self):
        """test for max int"""
        self.assertEqual(max_integer([99, 55, 21, 54, 55, 155, 10,
                                      21, 54, 55, 155]), 155)

    def test_negative(self):
        """test for max int"""
        self.assertEqual(max_integer([99, -55, 21, 54, -55, 155, -10]), 155)

    def test_intandfloat(self):
        """test for max int"""
        self.assertEqual(max_integer([99, 55, 21, 54, 55, 155.2, 10]), 155.2)

    def test_float(self):
        """test for max int"""
        self.assertEqual(max_integer([99.2, 55.5, 21.1, 54.4, 55.5,
                                      155.2, 10.1]), 155.2)

    def test_floatbig(self):
        """test for max int"""
        self.assertEqual(max_integer([99.5151354, 55.25435435453,
                                      21.54654638543, 54.2453453,
                                      55.54654536, 155.2,
                                      10.546543]), 155.2)

    def test_stringnum(self):
        """test for max int"""
        self.assertEqual(max_integer("1548468454159"), "9")

    def test_string(self):
        """test for max int"""
        self.assertEqual(max_integer("albert"), "t")

    def test_list(self):
        """test for max int"""
        self.assertEqual(max_integer([[], [2], [4], [2, 9]]), [4])

    def test_infin(self):
        """test for max int"""
        self.assertEqual(max_integer([10, float('inf'),
                         float('-inf'), 22]), float('inf'))

    def test_nan(self):
        """test for max int"""
        self.assertEqual(max_integer([10, float('nan'), 22]), 22)

    def test_mix(self):
        """test for max int"""
        with self.assertRaises(TypeError):
            max_integer([[], [6], [5], [5, 10], 22, "hey"])

    def test_mix2(self):
        """test for max int"""
        with self.assertRaises(TypeError):
            max_integer([6, "hey"])

    def test_none(self):
        """test for max int"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_inte(self):
        """test for max int"""
        with self.assertRaises(TypeError):
            max_integer(22)

    def test_floater(self):
        """test for max int"""
        with self.assertRaises(TypeError):
            max_integer(5.55)

    def test_dico(self):
        """test for max int"""
        with self.assertRaises(TypeError):
            max_integer([{55: 21, 55: 544}, {"hey", "how"}])


if __name__ == '__main__':
    unittest.main()
