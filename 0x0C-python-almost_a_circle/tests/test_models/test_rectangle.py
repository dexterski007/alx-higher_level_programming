#!/usr/bin/python3
""" unittest for rectaangle """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from contextlib import redirect_stdout
import io

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

    def test4_instant(self):
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

    def test5_instant(self):
        """ test instant """
        rect1 = Rectangle(5, 10, 55, 20)
        msg = {'_Rectangle__height': 10, '_Rectangle__width': 5,
             '_Rectangle__x': 55, '_Rectangle__y': 20, 'id': 1}
        self.assertEqual(rect1.__dict__, msg)

        rect1 = Rectangle(5, 10, 55, 20, 2)
        msg = {'_Rectangle__height': 10, '_Rectangle__width': 5,
             '_Rectangle__x': 55, '_Rectangle__y': 20, 'id': 2}
        self.assertEqual(rect1.__dict__, msg)

    def test6_instant(self):
        """ test instant """
        rec1 = Rectangle(55, 444, id=421, y=99, x=101)
        msg = {'_Rectangle__height': 444, '_Rectangle__width': 55,
             '_Rectangle__x': 101, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(rec1.__dict__, msg)

    def test7_inheritance(self):
        """ test inheritance """
        Base._Base__nb_objects = 10
        rec1 = Rectangle(3, 4)
        self.assertEqual(rec1.id, 11)

    def test8_properties(self):
        """ test getter setter """
        rec1 = Rectangle(5, 9)
        rec1.width = 5
        rec1.height = 6
        rec1.x = 7
        rec1.y = 8
        msg = {'_Rectangle__height': 6, '_Rectangle__width': 5,
             '_Rectangle__x': 7, '_Rectangle__y': 8, 'id': 1}
        self.assertEqual(rec1.__dict__, msg)
        self.assertEqual(rec1.width, 5)
        self.assertEqual(rec1.height, 6)
        self.assertEqual(rec1.x, 7)
        self.assertEqual(rec1.y, 8)

    def varioustypes(self):
        """ test for tuples """
        t = (3.16, -1.1, float('inf'), float('-inf'), False, "xsfg", (2,),
             [6], {6}, {6: 7}, None)
        return t

    def test10_validate(self):
        """ test validation """
        rec1 = Rectangle(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            msg = "{} must be an integer".format(attribute)
            for invalid_type in self.varioustypes():
                with self.assertRaises(TypeError) as excp:
                    setattr(rec1, attribute, invalid_type)
                self.assertEqual(str(excp.exception), msg)

    def test11_negaative(self):
        """ test negative """
        rec1 = Rectangle(1, 2)
        attributes = ["width", "height"]
        for attribute in attributes:
            msg = "{} must be > 0".format(attribute)
            with self.assertRaises(ValueError) as excp:
                setattr(rec1, attribute, -(15 + 1))
            self.assertEqual(str(excp.exception), msg)

    def test12_negativexy(self):
        """ test xy"""
        rec1 = Rectangle(1, 2)
        attributes = ["x", "y"]
        for attribute in attributes:
            msg = "{} must be >= 0".format(attribute)
            with self.assertRaises(ValueError) as excp:
                setattr(rec1, attribute, -(15 + 1))
            self.assertEqual(str(excp.exception), msg)

    def test13_zero(self):
        """ test width height """
        rec1 = Rectangle(1, 2)
        attributes = ["width", "height"]
        for attribute in attributes:
            msg = "{} must be > 0".format(attribute)
            with self.assertRaises(ValueError) as excp:
                setattr(rec1, attribute, 0)
            self.assertEqual(str(excp.exception), msg)

    def test14_getters(self):
        """ test getters """
        rec1 = Rectangle(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            n = 15 + 1
            setattr(rec1, attribute, n)
            self.assertEqual(getattr(rec1, attribute), n)

    def test15_range(self):
        """ test get set """
        rec1 = Rectangle(1, 2)
        rec1.x = 0
        rec1.y = 0
        self.assertEqual(rec1.x, 0)
        self.assertEqual(rec1.y, 0)

    def test16_area(self):
        """ test area """
        rec = Rectangle(5, 6)
        with self.assertRaises(TypeError) as e:
            Rectangle.area()
        msg = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test17_area(self):
        """ test areaaa"""
        rec = Rectangle(5, 6)
        self.assertEqual(rec.area(), 30)
        wid = 66 + 1
        heig = 66 + 1
        rec.width = wid
        rec.height = heig
        self.assertEqual(rec.area(), wid * heig)
        wid = 85 + 1
        heig = 64 + 1
        rec = Rectangle(wid, heig, 7, 8, 9)
        self.assertEqual(rec.area(), wid * heig)
        wid = 15 + 1
        heig = 15 + 1
        rec = Rectangle(wid, heig, y=7, x=8, id=9)
        self.assertEqual(rec.area(), wid * heig)

        rec1 = Rectangle(3, 2)
        self.assertEqual(rec1.area(), 6)

        rec2 = Rectangle(2, 10)
        self.assertEqual(rec2.area(), 20)

        rec3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(rec3.area(), 56)

    def test18_displ(self):
        """ test display"""
        rec = Rectangle(9, 8)
        with self.assertRaises(TypeError) as e:
            Rectangle.display()
        msg = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_J_display_simple(self):
        '''Tests display() method output.'''
        rec = Rectangle(1, 1)
        outp = io.StringIO()
        with redirect_stdout(outp):
            rec.display()
        msg = "#\n"
        self.assertEqual(outp.getvalue(), msg)
        rec.width = 3
        rec.height = 5
        outp = io.StringIO()
        with redirect_stdout(outp):
            rec.display()
        msg = "\
###\n\
###\n\
###\n\
###\n\
###\n\
"
        self.assertEqual(outp.getvalue(), msg)
        rec = Rectangle(5, 6, 7, 8)
        outp = io.StringIO()
        with redirect_stdout(outp):
            rec.display()
        msg = """







       #####
       #####
       #####
       #####
       #####
       #####
"""
        self.assertEqual(outp.getvalue(), msg)


if __name__ == "__main__":
    unittest.main()
