#!/usr/bin/python3
""" first class """
import json
import csv


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """ instantiation """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ json exporter """
        if not list_dictionaries or list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file """
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ json importer """
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ new instance """
        from .rectangle import Rectangle
        from .square import Square
        if cls is Rectangle:
            dummy = Rectangle(1, 1)
        elif cls is Square:
            dummy = Square(1)
        else:
            dummy = None

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """ load instance from json """
        from os import path
        filename = cls.__name__ + ".json"
        if not path.isfile(filename):
            return []
        with open(filename, mode="r", encoding="utf-8") as file:
            return [cls.create(**inst) for inst\
                    in cls.from_json_string(file.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serialize to csv """
        from .rectangle import Rectangle
        from .square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[obj.id, obj.width, obj.height, obj.x,
                              obj.y] for obj in list_objs]
            else:
                list_objs = [[obj.id, obj.size, obj.x, obj.y] for\
                              obj in list_objs]
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", encoding="utf-8", newline ='') as file:
            writer = csv.writer(file)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """ deserialize from csv """
        from .rectangle import Rectangle
        from .square import Square
        filename = cls.__name__ + ".csv"
        export = []
        with open(filename, mode="r", encoding="utf-8", newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                row = [int(col) for col in row]
                if cls is Rectangle:
                    dic = {"id": row[0], "width": row[1], "height": row[2],
                           "x": row[3], "y": row[4]}
                else:
                    dic = {"id": row[0], "size": row[1], "x": row[2],
                           "y": row[3]}
                export.append(cls.create(**dic))
        return export

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ turtle drawer """
        import turtle
        import time

        turtle.getscreen()
        t.title("Shape drawer")
        for s in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.pensize(10)
            t.penup()
            t.setpos(s.x + t.pos()[0], s.y + t.pos([1]))
            t.pendown()
            t.beginfill()
            t.fd(s.width)
            t.left(90)
            t.fd(s.height)
            t.left(90)
            t.fd(s.width)
            t.left(90)
            t.fd(s.height)
            t.left(90)
            t.endfill()
        time.sleep()


            
