#!/usr/bin/python3
""" rectangle class """
from .base import Base


class Rectangle(Base):
    """ rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ instantiation """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        self.integ_validator("width", value, True)
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        self.integ_validator("height", value, True)
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        self.integ_validator("x", value, False)
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        self.integ_validator("y", value, False)
        self.__y = value

    def integ_validator(self, name, value, flag):
        """ int validate """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0 and flag:
            raise ValueError("{} must be > 0".format(name))
        if value < 0 and not flag:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """ area calculator """
        return self.width * self.height

    def display(self):
        """ shape printer """
        shape = ""
        shape += ('\n' * self.y)
        for i in range(self.height):
            shape += (' ' * self.x)
            for j in range(self.width):
                shape += "#"
            shape += '\n'
        print(shape, end="")

    def __str__(self):
        """ override str """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.x, self.y, self.width,
                    self.height))

    def __update(self, id=None, width=None,
                 height=None, x=None, y=None):
        """ args handler """
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """ update rect """
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """ return dictionary """
        dic = {'id': self.id, 'width': self.width,
               'height': self.height, 'x': self.x, 'y': self.y}
        return dic
