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
            self.assertEqual(Base.to_json_string(None), "[]")
            self.assertEqual(Base.to_json_string([]), "[]")
            data = [{'x': 45646, 'y': 2128, 'width': 5132, 'id': 8754,
             'height': 51233}]
            self.assertEqual(len(Base.to_json_string(data)), len(str(data)))
            data = [{"testinghey": 21324545}]
            self.assertEqual(Base.to_json_string(data),
                             '[{"testinghey": 21324545}]')
            data = [{"testinghey": 21324545}, {"heyehey": 243543},
                    {"HOOgfdf": 0}]
            self.assertEqual(Base.to_json_string(data),
                             '[{"testinghey": 21324545}, {"heyehey": 243543},\
                             {"HOOgfdf": 0}]')
            data = [{'x': 6, 'y': 22, 'width': 5, 'id': 2, 'height': 4},
                    {'x': 25, 'y': 24, 'width': 255, 'id': 212,
                    'height': 455}]
            self.assertEqual(len(Base.to_json_string(data)), len(str(data)))
            data = [{}]
            self.assertEqual(Base.to_json_string(data), '[{}]')
            st2 = [{}, {}]
            self.assertEqual(Base.to_json_string(data), '[{}, {}]')

            rec1 = Rectangle(22, 8, 6, 10)
            dicti = rec1.to_dictionary()
            json_dictionary = Base.to_json_string([dicti])
            dicti = str([dicti])
            dicti = dicti.replace("'", '"')
            self.assertEqual(dicti, json_dictionary)

            rec1 = Rectangle(22, 8, 6, 10)
            rec2 = Rectangle(6, 4, 3, 3)
            rec3 = Rectangle(5, 3, 2, 5)
            dicti = [rec1.to_dictionary(), rec2.to_dictionary(),
                          rec3.to_dictionary()]
            json_dictionary = Base.to_json_string(dicti)
            dicti = str(dicti)
            dicti = dicti.replace("'", '"')
            self.assertEqual(dicti, json_dictionary)

            rec1 = Square(10, 7, 2)
            dicti = rec1.to_dictionary()
            json_dictionary = Base.to_json_string([dicti])
            dicti = str([dicti])
            dicti = dicti.replace("'", '"')
            self.assertEqual(dicti, json_dictionary)

            rec1 = Square(10, 7, 2)
            rec2 = Square(1, 2, 3)
            rec3 = Square(2, 3, 4)
            dicti = [rec1.to_dictionary(), rec2.to_dictionary(),
                          rec3.to_dictionary()]
            json_dictionary = Base.to_json_string(dicti)
            dicti = str(dicti)
            dicti = dicti.replace("'", '"')
            self.assertEqual(dicti, json_dictionary)

    def test_fromjson(self):
        """ json import """
        with self.assertRaises(TypeError) as excep:
            Base.from_json_string()
        err = "from_json_string() missing 1 required positional argument: \
'json_string'"
        self.assertEqual(str(excep.exception), err)

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        st1 = '[{"x": 10, "y": 12, "width": 13, "id": 14, "height": 5}, \
              {"x": 54, "y": 231, "width": 54, "id": 8978, \
              "height": 215}]'
        st2= [{'x': 10, 'y': 12, 'width': 13, 'id': 14, 'height': 5}, \
              {'x': 54, 'y': 231, 'width': 54, 'id': 8978,
             'height': 215}]
        self.assertEqual(Base.from_json_string(st1), st2)

        st1 = [{}, {}]
        st2 = '[{}, {}]'
        self.assertEqual(Base.from_json_string(st1), st2)
        st2 = [{}]
        st1 = '[{}]'
        self.assertEqual(Base.from_json_string(st1), st2)

        st2 = [{"hello": 9696696969}, {"world": 123}, {"HEY": 0}]
        st1 = '[{"hello": 9696696969}, {"world": 123}, {"HI": 0}]'
        self.assertEqual(Base.from_json_string(st1), st2)

        st2 = [{"hello": 9696696969}]
        st1 = '[{"hello": 9696696969}]'
        self.assertEqual(Base.from_json_string(st1), st2)

        st2 = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        st1 = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}]'
        self.assertEqual(Base.from_json_string(st1), st2)

        st2 = [{'x': 513, 'y': 125, 'width': 524, 'id': 2544,
             'height': 2522}]
        st1 = '[{"x": 513, "y": 125, "width": 524, "id": 2544, \
                "height": 2522}]'
        self.assertEqual(Base.from_json_string(st1), st2)

        list1 = [
            {'id': 55, 'width': 44, 'height': 11},
            {'id': 4, 'width': 1, 'height': 7}
        ]
        list2 = Rectangle.from_json_string(
            Rectangle.to_json_string(list1))
        self.assertEqual(list1, list2)

    def test_I_save_to_file(self):
        '''Tests save_to_file() method.'''
        import os
        rec1 = Rectangle(15, 7, 2, 8)
        rec2 = Rectangle(2, 2)
        Rectangle.save_to_file([rec1, rec2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 105)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        rec2 = Rectangle(2, 4)
        Rectangle.save_to_file([rec2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 52)

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Square.json")
        except:
            pass
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        rec2 = Square(1)
        Square.save_to_file([rec2])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 38)

    def test_create(self):
        ''' test create '''
        rec1 = Rectangle(3, 5, 1)
        rec1_dictionary = rec1.to_dictionary()
        rec2 = Rectangle.create(**rec1_dictionary)
        self.assertEqual(str(rec1), str(rec2))
        self.assertFalse(rec1 is rec2)
        self.assertFalse(rec1 == rec2)

    def test_loadfile(self):
        ''' load form file '''
        rec1 = Rectangle(10, 7, 2, 8)
        rec2 = Rectangle(2, 4)
        list1 = [rec1, rec2]
        Rectangle.save_to_file(list1)
        list2 = Rectangle.load_from_file()
        self.assertNotEqual(id(list1[0]), id(list2[0]))
        self.assertEqual(str(list1[0]), str(list2[0]))
        self.assertNotEqual(id(list1[1]), id(list2[1]))
        self.assertEqual(str(list1[1]), str(list2[1]))

        sq1 = Square(5)
        sq2 = Square(7, 9, 1)
        list1 = [sq1, sq2]
        Square.save_to_file(list1)
        list2 = Square.load_from_file()
        self.assertNotEqual(id(list1[0]), id(list2[0]))
        self.assertEqual(str(list1[0]), str(list2[0]))
        self.assertNotEqual(id(list1[1]), id(list2[1]))
        self.assertEqual(str(list1[1]), str(list2[1]))




if __name__ == "__main__":
    unittest.main()
