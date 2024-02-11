#!/usr/bin/python3
""" unittest for rectaangle """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class testingrect(unittest.TestCase):
    """ test rectangle """

    def setUp(self):
        """ startup routine """
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """ cleaning routine """
        pass

    def test1(self):
        """ test type """
        self.assertEqual(str(Rectangle), "<class 'models.rectangle.Rectangle'>")

    def test2(self):
        """ test inheritance """
        self.assertTrue(issubclass(Rectangle, Base))

    def test3(self):
        """test constructor"""
        with self.assertRaises(TypeError) as excp:
            rec = Rectangle()
        msg = "__init__() missing 2 required positional arguments: 'width' \
and 'height'"
        self.assertEqual(str(excp.exception), msg)

    def test_D_instantiation(self):
        """ test instant"""
        rec1 = Rectangle(66, 55)
        self.assertEqual(str(type(rec1)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(rec1, Base))
        tab = {'_Rectangle__height': 55, '_Rectangle__width': 66,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(rec1.__dict__, tab)

        with self.assertRaises(TypeError) as excp:
            rec1 = Rectangle("sfsg", 2)
        msg = "width must be an integer"
        self.assertEqual(str(excp.exception), msg)

        with self.assertRaises(TypeError) as excp:
            rec1 = Rectangle(1, "sfgsfg")
        msg = "height must be an integer"
        self.assertEqual(str(excp.exception), msg)

        with self.assertRaises(TypeError) as excp:
            rec1 = Rectangle(1, 2, "sfgsfg")
        msg = "x must be an integer"
        self.assertEqual(str(excp.exception), msg)

        with self.assertRaises(TypeError) as excp:
            rec1 = Rectangle(1, 2, 3, "sfgsfg")
        msg = "y must be an integer"
        self.assertEqual(str(excp.exception), msg)

        with self.assertRaises(ValueError) as excp:
            rec1 = Rectangle(-5, 2)
        msg = "width must be > 0"
        self.assertEqual(str(excp.exception), msg)

        with self.assertRaises(ValueError) as excp:
            rec1 = Rectangle(15, -5)
        msg = "height must be > 0"
        self.assertEqual(str(excp.exception), msg)

        with self.assertRaises(ValueError) as excp:
            rec1 = Rectangle(0, 58)
        msg = "width must be > 0"
        self.assertEqual(str(excp.exception), msg)

        with self.assertRaises(ValueError) as excp:
            rec1 = Rectangle(55, 0)
        msg = "height must be > 0"
        self.assertEqual(str(excp.exception), msg)

        with self.assertRaises(ValueError) as excp:
            rec1 = Rectangle(1, 99, -54)
        msg = "x must be >= 0"
        self.assertEqual(str(excp.exception), msg)

        with self.assertRaises(ValueError) as excp:
            rec1 = Rectangle(1, 12, 3, -65)
        msg = "y must be >= 0"
        self.assertEqual(str(excp.exception), msg)


if __name__ == "__main__":
    unittest.main()
