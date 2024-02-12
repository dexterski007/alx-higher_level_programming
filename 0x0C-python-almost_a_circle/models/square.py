#!/usr/bin/python3
""" spongebob class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ instantiation """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ print method """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.width))

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """update handler """
        if id is not None:
            self.id = id
        if size is not None:
            self.width = size
            self.height = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """ update values """
        if args:
            self.__update(*args)
        if kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """ return dictionary square """
        dic = {'id': self.id, 'size': self.size,
               'x': self.x, 'y': self.y}
        return dic
