#!/usr/bin/python3
""" unittest for base """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class testingbase(unittest.TestCase):
    """ test base """

    def setUp(self):
        """ startup routine """
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """ cleaning routine """
        pass

    def test1(self):
        """ test base init 0 """
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test2(self):
        """ test private class """
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test3(self):
        """ test instantiation """
        getb = Base()
        self.assertEqual(str(type(getb)), "<class 'models.base.Base'>")
        self.assertEqual(getb.__dict__, {"id": 1})
        self.assertEqual(getb.id, 1)

    def test4(self):
        """ test 2 ids """
        getb1 = Base()
        getb2 = Base()
        self.assertEqual(getb1.id + 1, getb2.id)

    def test5(self):
        """ test custom id """
        value = 7
        getb = Base(value)
        self.assertEqual(getb.id, value)

    def test6(self):
        """ test custom id str """
        value = "val"
        getb = Base(value)
        self.assertEqual(getb.id, value)

    def test_tojson(self):
        """ test to json """
        with self.assertRaises(TypeError) as err:
            Base.to_json_string()
            string = "to_json_string() missing 1 required positional argument: \
                      'list_dictionaries'"
            self.assertEqual(string, str(err.exception))








if __name__ == "__main__":
    unittest.main()
