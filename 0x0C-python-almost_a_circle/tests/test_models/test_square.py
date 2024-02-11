#!/usr/bin/python3
""" unittest for rectaangle """
import unittest
from models.base import Base
from models.square import Square
from contextlib import redirect_stdout
import io

class testingsqu(unittest.TestCase):
    """ test square """

    def setUp(self):
        """ startup routine """
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """ cleaning routine """
        pass

    def test1_class(self):
        """ test class type """
        self.assertEqual(str(Square), "<class 'models.square.Square'>")

    def test2_inheritance(self):
        """ test inheritance """
        self.assertTrue(issubclass(Square, Base))

    def test3_instant(self):
        """ test instantiation """
        rec = Square(5)
        self.assertEqual(str(type(rec)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(rec, Base))
        dicti = {'_Rectangle__height': 5, '_Rectangle__width': 5,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(rec.__dict__, dicti)

        with self.assertRaises(TypeError) as excp:
            rec = Square("1")
        msg = "width must be an integer"
        self.assertEqual(str(excp.exception), msg)

        with self.assertRaises(TypeError) as excp:
            rec = Square(1, "dfdf")
        msg = "x must be an integer"
        self.assertEqual(str(excp.exception), msg)

        with self.assertRaises(TypeError) as excp:
            rec = Square(1, 2, "sgsfg")
        msg = "y must be an integer"
        self.assertEqual(str(excp.exception), msg)

        with self.assertRaises(ValueError) as excp:
            rec = Square(-545)
        msg = "width must be > 0"
        self.assertEqual(str(excp.exception), msg)

        with self.assertRaises(ValueError) as excp:
            rec = Square(1, -546)
        msg = "x must be >= 0"
        self.assertEqual(str(excp.exception), msg)

        with self.assertRaises(ValueError) as excp:
            rec = Square(1, 2, -545)
        msg = "y must be >= 0"
        self.assertEqual(str(excp.exception), msg)

        with self.assertRaises(ValueError) as excp:
            rec = Square(0)
        msg = "width must be > 0"
        self.assertEqual(str(excp.exception), msg)

    def test4_instant(self):
        """ test instant """
        rec = Square(5, 55, 15)
        dicti = {'_Rectangle__height': 5, '_Rectangle__width': 5,
             '_Rectangle__x': 55, '_Rectangle__y': 15, 'id': 1}
        self.assertEqual(rec.__dict__, dicti)

        rec = Square(5, 10, 15, 20)
        dicti = {'_Rectangle__height': 5, '_Rectangle__width': 5,
             '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 20}
        self.assertEqual(rec.__dict__, dicti)

    def test5_instant(self):
        """ test instant """
        rec = Square(55, id=421, y=99, x=22)
        dicti = {'_Rectangle__height': 55, '_Rectangle__width': 55,
             '_Rectangle__x': 22, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(rec.__dict__, dicti)

    def test6_instant(self):
        """ test instant """
        Base._Base__nb_objects = 55
        rec = Square(2)
        self.assertEqual(rec.id, 56)

    def test7_properties(self):
        """ test getters setters """
        rec = Square(5, 9)
        rec.size = 98
        rec.x = 102
        rec.y = 103
        dicti = {'_Rectangle__height': 98, '_Rectangle__width': 98,
             '_Rectangle__x': 102, '_Rectangle__y': 103, 'id': 1}
        self.assertEqual(rec.__dict__, dicti)
        self.assertEqual(rec.size, 98)
        self.assertEqual(rec.x, 102)
        self.assertEqual(rec.y, 103)

    # ----------------- Tests for #3 ------------------------

    def testing_types(self):
        """ values for test """
        typ = (3.15, -1.1, float('inf'), float('-inf'), False, "str", (2,),
             [4], {5}, {6: 7}, None)
        return typ

    def test8_valid(self):
        """ validation """
        rec = Square(1)
        attributes = ["x", "y"]
        for attribute in attributes:
            msg = "{} must be an integer".format(attribute)
            for invalid_type in self.testing_types():
                with self.assertRaises(TypeError) as excp:
                    setattr(rec, attribute, invalid_type)
                self.assertEqual(str(excp.exception), msg)
        msg = "width must be an integer"
        for invalid_type in self.testing_types():
            with self.assertRaises(TypeError) as excp:
                setattr(rec, "width", invalid_type)
            self.assertEqual(str(excp.exception), msg)

    def test9_negative(self):
        """ test validation """
        rec = Square(1, 2)
        attributes = ["size"]
        for attribute in attributes:
            msg = "width must be > 0".format(attribute)
            with self.assertRaises(ValueError) as excp:
                setattr(rec, attribute, -(15 + 1))
            self.assertEqual(str(excp.exception), msg)

    def test10_validation(self):
        """ validation properties """
        rec = Square(1, 2)
        attributes = ["x", "y"]
        for attribute in attributes:
            msg = "{} must be >= 0".format(attribute)
            with self.assertRaises(ValueError) as excp:
                setattr(rec, attribute, -(15 + 1))
            self.assertEqual(str(excp.exception), msg)

    def test11_zero(self):
        """ zero validate """
        rec = Square(1, 2)
        attributes = ["size"]
        for attribute in attributes:
            msg = "width must be > 0".format(attribute)
            with self.assertRaises(ValueError) as excp:
                setattr(rec, attribute, 0)
            self.assertEqual(str(excp.exception), msg)

    def test12_property(self):
        """ test getter setter"""
        rec = Square(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            n = 15 + 1
            setattr(rec, attribute, n)
            self.assertEqual(getattr(rec, attribute), n)

    def test13_zero(self):
        """ test getter setter """
        rec = Square(1, 2)
        rec.x = 0
        rec.y = 0
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)

    def test14_area(self):
        """ tests area """
        rec = Square(5)
        with self.assertRaises(TypeError) as excp:
            Square.area()
        msg = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excp.exception), msg)

    def test15_area(self):
        """ test area """
        rec = Square(6)
        self.assertEqual(rec.area(), 36)
        wid = 15 + 1
        rec.size = wid
        self.assertEqual(rec.area(), wid * wid)
        wid = 15 + 1
        rec = Square(wid, 7, 8, 9)
        self.assertEqual(rec.area(), wid * wid)
        wid = 15 + 1
        rec = Square(wid, y=7, x=8, id=9)
        self.assertEqual(rec.area(), wid * wid)

        Base._Base__nb_objects = 0
        squ1 = Square(5)
        self.assertEqual(str(squ1), "[Square] (1) 0/0 - 5")
        self.assertEqual(squ1.size, 5)
        squ1.size = 10
        self.assertEqual(str(squ1), "[Square] (1) 0/0 - 10")
        self.assertEqual(squ1.size, 10)

        with self.assertRaises(TypeError) as excp:
            squ1.size = "9"
        self.assertEqual(str(excp.exception), "width must be an integer")

        with self.assertRaises(ValueError) as excp:
            squ1.size = 0
        self.assertEqual(str(excp.exception), "width must be > 0")

    def test16_noargs(self):
        """ test display """
        rec = Square(9)
        with self.assertRaises(TypeError) as excp:
            Square.display()
        msg = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excp.exception), msg)

    def test17_display(self):
        """ tests display """
        rec = Square(1)
        fout = io.StringIO()
        with redirect_stdout(fout):
            rec.display()
        msg = "#\n"
        self.assertEqual(fout.getvalue(), msg)
        rec.size = 3
        fout = io.StringIO()
        with redirect_stdout(fout):
            rec.display()
        msg = "\
###\n\
###\n\
###\n\
"
        self.assertEqual(fout.getvalue(), msg)
        rec = Square(5, 6, 7)
        fout = io.StringIO()
        with redirect_stdout(fout):
            rec.display()
        msg = """\







      #####
      #####
      #####
      #####
      #####
"""
        self.assertEqual(fout.getvalue(), msg)

    def test18_method(self):
        """ tests methods """
        rec = Square(5, 2)
        with self.assertRaises(TypeError) as excp:
            Square.__str__()
        msg = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excp.exception), msg)

    def test19_method(self):
        """ test methods """
        rec = Square(5)
        msg = '[Square] (1) 0/0 - 5'
        self.assertEqual(str(rec), msg)
        rec = Square(1, 1)
        msg = '[Square] (2) 1/0 - 1'
        self.assertEqual(str(rec), msg)
        rec = Square(3, 4, 5)
        msg = '[Square] (3) 4/5 - 3'
        self.assertEqual(str(rec), msg)
        rec = Square(10, 20, 30, 40)
        msg = '[Square] (40) 20/30 - 10'
        self.assertEqual(str(rec), msg)

    def test20_update(self):
        """ test update"""
        rec = Square(5, 2)
        with self.assertRaises(TypeError) as excp:
            Square.update()
        msg = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excp.exception), msg)

        dicti = rec.__dict__.copy()
        rec.update()
        self.assertEqual(rec.__dict__, dicti)

    def test21_update(self):
        """ test update """
        rec = Square(5, 2)
        dicti = rec.__dict__.copy()

        rec.update(10)
        dicti["id"] = 10
        self.assertEqual(rec.__dict__, dicti)

        rec.update(10, 5)
        dicti["_Rectangle__height"] = 5
        dicti["_Rectangle__width"] = 5
        self.assertEqual(rec.__dict__, dicti)

        rec.update(10, 5, 20)
        dicti["_Rectangle__x"] = 20
        self.assertEqual(rec.__dict__, dicti)

        rec.update(10, 5, 20, 25)
        dicti["_Rectangle__y"] = 25
        self.assertEqual(rec.__dict__, dicti)

    def test22_badargs(self):
        """ test update with bad args"""
        rec = Square(5, 2)
        dicti = rec.__dict__.copy()

        rec.update(10)
        dicti["id"] = 10
        self.assertEqual(rec.__dict__, dicti)

        with self.assertRaises(ValueError) as excp:
            rec.update(10, -5)
        msg = "width must be > 0"
        self.assertEqual(str(excp.exception), msg)

        with self.assertRaises(ValueError) as excp:
            rec.update(10, 5, -17)
        msg = "x must be >= 0"
        self.assertEqual(str(excp.exception), msg)

        with self.assertRaises(ValueError) as excp:
            rec.update(10, 5, 17, -25)
        msg = "y must be >= 0"
        self.assertEqual(str(excp.exception), msg)

    def test23_kwargs(self):
        """ testing kwargs """
        rec = Square(5, 2)
        dicti = rec.__dict__.copy()

        rec.update(id=10)
        dicti["id"] = 10
        self.assertEqual(rec.__dict__, dicti)

        rec.update(size=17)
        dicti["_Rectangle__height"] = 17
        dicti["_Rectangle__width"] = 17
        self.assertEqual(rec.__dict__, dicti)

        rec.update(x=20)
        dicti["_Rectangle__x"] = 20
        self.assertEqual(rec.__dict__, dicti)

        rec.update(y=25)
        dicti["_Rectangle__y"] = 25
        self.assertEqual(rec.__dict__, dicti)

    def test24_kwargs(self):
        """ test update """
        rec = Square(5, 2)
        dicti = rec.__dict__.copy()

        rec.update(id=10)
        dicti["id"] = 10
        self.assertEqual(rec.__dict__, dicti)

        rec.update(id=10, size=5)
        dicti["_Rectangle__height"] = 5
        dicti["_Rectangle__width"] = 5
        self.assertEqual(rec.__dict__, dicti)

        rec.update(id=10, size=5, x=20)
        dicti["_Rectangle__x"] = 20
        self.assertEqual(rec.__dict__, dicti)

        rec.update(id=10, size=5, x=20, y=25)
        dicti["_Rectangle__y"] = 25
        self.assertEqual(rec.__dict__, dicti)

        rec.update(y=25, id=10, x=20, size=5)
        self.assertEqual(rec.__dict__, dicti)

        Base._Base__nb_objects = 0
        squ1 = Square(5)
        self.assertEqual(str(squ1), "[Square] (1) 0/0 - 5")

        squ1.update(10)
        self.assertEqual(str(squ1), "[Square] (10) 0/0 - 5")

        squ1.update(1, 2)
        self.assertEqual(str(squ1), "[Square] (1) 0/0 - 2")

        squ1.update(1, 2, 3)
        self.assertEqual(str(squ1), "[Square] (1) 3/0 - 2")

        squ1.update(1, 2, 3, 4)
        self.assertEqual(str(squ1), "[Square] (1) 3/4 - 2")

        squ1.update(x=12)
        self.assertEqual(str(squ1), "[Square] (1) 12/4 - 2")

        squ1.update(size=7, y=1)
        self.assertEqual(str(squ1), "[Square] (1) 12/1 - 7")

        squ1.update(size=7, id=89, y=1)
        self.assertEqual(str(squ1), "[Square] (89) 12/1 - 7")

    def test25_todict(self):
        """ test dict """
        with self.assertRaises(TypeError) as excp:
            Square.to_dictionary()
        msg = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excp.exception), msg)

        rec = Square(1)
        dicti = {'x': 0, 'y': 0, 'size': 1, 'id': 1}
        self.assertEqual(rec.to_dictionary(), dicti)

        rec = Square(9, 2, 3, 4)
        dicti = {'x': 2, 'y': 3, 'size': 9, 'id': 4}
        self.assertEqual(rec.to_dictionary(), dicti)

        rec.x = 10
        rec.y = 20
        rec.size = 30
        dicti = {'x': 10, 'y': 20, 'size': 30, 'id': 4}
        self.assertEqual(rec.to_dictionary(), dicti)

        squ1 = Square(10, 2, 1)
        s1_dictionary = squ1.to_dictionary()
        squ2 = Square(1, 1)
        squ2.update(**s1_dictionary)
        self.assertEqual(str(squ1), str(squ2))
        self.assertNotEqual(squ1, squ2)


if __name__ == "__main__":
    unittest.main()
