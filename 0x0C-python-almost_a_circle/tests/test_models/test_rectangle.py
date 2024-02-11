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
        with self.assertRaises(TypeError) as excp:
            Rectangle.area()
        msg = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excp.exception), msg)

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
        with self.assertRaises(TypeError) as excp:
            Rectangle.display()
        msg = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excp.exception), msg)

    def test19_displ(self):
        """ test display """
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

    def test20_posit(self):
        """ test posit """
        rec = Rectangle(5, 2)
        with self.assertRaises(TypeError) as excp:
            Rectangle.__str__()
        msg = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excp.exception), msg)

    def test21_posit(self):
        """ test posit """
        rec = Rectangle(5, 2)
        msg = '[Rectangle] (1) 0/0 - 5/2'
        self.assertEqual(str(rec), msg)
        rec = Rectangle(1, 1, 1)
        msg = '[Rectangle] (2) 1/0 - 1/1'
        self.assertEqual(str(rec), msg)
        rec = Rectangle(3, 4, 5, 6)
        msg = '[Rectangle] (3) 5/6 - 3/4'
        self.assertEqual(str(rec), msg)

        Base._Base__nb_objects = 0
        rec1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(rec1), "[Rectangle] (12) 2/1 - 4/6")

        rec2 = Rectangle(5, 5, 1)
        self.assertEqual(str(rec2), "[Rectangle] (1) 1/0 - 5/5")

    def test22_update(self):
        """ test update """
        rec = Rectangle(6, 2)
        with self.assertRaises(TypeError) as excp:
            Rectangle.update()
        msg = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excp.exception), msg)

        dicti = rec.__dict__.copy()
        rec.update()
        self.assertEqual(rec.__dict__, dicti)

    def test23_updateargs(self):
        """ test updaate """
        rec = Rectangle(15, 2)
        dicti = rec.__dict__.copy()

        rec.update(10)
        dicti["id"] = 10
        self.assertEqual(rec.__dict__, dicti)

        rec.update(10, 5)
        dicti["_Rectangle__width"] = 5
        self.assertEqual(rec.__dict__, dicti)

        rec.update(10, 5, 17)
        dicti["_Rectangle__height"] = 17
        self.assertEqual(rec.__dict__, dicti)

        rec.update(10, 5, 17, 20)
        dicti["_Rectangle__x"] = 20
        self.assertEqual(rec.__dict__, dicti)

        rec.update(10, 5, 17, 20, 25)
        dicti["_Rectangle__y"] = 25
        self.assertEqual(rec.__dict__, dicti)

    def test24_testargs(self):
        """ test update args """
        rec = Rectangle(5, 2)
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
        msg = "height must be > 0"
        self.assertEqual(str(excp.exception), msg)

        with self.assertRaises(ValueError) as excp:
            rec.update(10, 5, 17, -20)
        msg = "x must be >= 0"
        self.assertEqual(str(excp.exception), msg)

        with self.assertRaises(ValueError) as excp:
            rec.update(10, 5, 17, 20, -25)
        msg = "y must be >= 0"
        self.assertEqual(str(excp.exception), msg)

    def test25_update(self):
        """ test update args """
        rec = Rectangle(5, 2)
        dicti = rec.__dict__.copy()

        rec.update(id=10)
        dicti["id"] = 10
        self.assertEqual(rec.__dict__, dicti)

        rec.update(width=5)
        dicti["_Rectangle__width"] = 5
        self.assertEqual(rec.__dict__, dicti)

        rec.update(height=17)
        dicti["_Rectangle__height"] = 17
        self.assertEqual(rec.__dict__, dicti)

        rec.update(x=20)
        dicti["_Rectangle__x"] = 20
        self.assertEqual(rec.__dict__, dicti)

        rec.update(y=25)
        dicti["_Rectangle__y"] = 25
        self.assertEqual(rec.__dict__, dicti)

    def test26_update(self):
        """ test kwargs """
        rec = Rectangle(5, 2)
        dicti = rec.__dict__.copy()

        rec.update(id=10)
        dicti["id"] = 10
        self.assertEqual(rec.__dict__, dicti)

        rec.update(id=10, width=5)
        dicti["_Rectangle__width"] = 5
        self.assertEqual(rec.__dict__, dicti)

        rec.update(id=10, width=5, height=17)
        dicti["_Rectangle__height"] = 17
        self.assertEqual(rec.__dict__, dicti)

        rec.update(id=10, width=5, height=17, x=20)
        dicti["_Rectangle__x"] = 20
        self.assertEqual(rec.__dict__, dicti)

        rec.update(id=10, width=5, height=17, x=20, y=25)
        dicti["_Rectangle__y"] = 25
        self.assertEqual(rec.__dict__, dicti)

        rec.update(y=25, id=10, height=17, x=20, width=5)
        self.assertEqual(rec.__dict__, dicti)

        Base._Base__nb_objects = 0
        rec1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(rec1), "[Rectangle] (1) 10/10 - 10/10")

        rec1.update(height=1)
        self.assertEqual(str(rec1), "[Rectangle] (1) 10/10 - 10/1")

        rec1.update(width=1, x=2)
        self.assertEqual(str(rec1), "[Rectangle] (1) 2/10 - 1/1")

        rec1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(rec1), "[Rectangle] (89) 3/1 - 2/1")

        rec1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(rec1), "[Rectangle] (89) 1/3 - 4/2")

        Base._Base__nb_objects = 0
        rec1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(rec1), "[Rectangle] (1) 10/10 - 10/10")

        rec1.update(89)
        self.assertEqual(str(rec1), "[Rectangle] (89) 10/10 - 10/10")

        rec1.update(89, 2)
        self.assertEqual(str(rec1), "[Rectangle] (89) 10/10 - 2/10")

        rec1.update(89, 2, 3)
        self.assertEqual(str(rec1), "[Rectangle] (89) 10/10 - 2/3")

        rec1.update(89, 2, 3, 4)
        self.assertEqual(str(rec1), "[Rectangle] (89) 4/10 - 2/3")

        rec1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(rec1), "[Rectangle] (89) 4/5 - 2/3")

    def test27_todict(self):
        """ test to dict"""
        with self.assertRaises(TypeError) as excp:
            Rectangle.to_dictionary()
        msg = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(excp.exception), msg)

        rec = Rectangle(1, 2)
        dicti = {'x': 0, 'y': 0, 'width': 1, 'id': 1, 'height': 2}
        self.assertEqual(rec.to_dictionary(), dicti)

        rec = Rectangle(1, 2, 3, 4, 5)
        dicti = {'x': 3, 'y': 4, 'width': 1, 'id': 5, 'height': 2}
        self.assertEqual(rec.to_dictionary(), dicti)

        rec.x = 10
        rec.y = 20
        rec.width = 30
        rec.height = 40
        dicti = {'x': 10, 'y': 20, 'width': 30, 'id': 5, 'height': 40}
        self.assertEqual(rec.to_dictionary(), dicti)

        rec1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = rec1.to_dictionary()
        rec2 = Rectangle(1, 1)
        rec2.update(**r1_dictionary)
        self.assertEqual(str(rec1), str(rec2))
        self.assertNotEqual(rec1, rec2)


if __name__ == "__main__":
    unittest.main()
