#!/usr/bin/python3
""" this is a class for reaading files """


class Student:
    """ class student """
    def __init__(self, first_name, last_name, age):
        """ instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ public method """
        try:
            for attribute in attrs:
                if type(attribute) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        new_dic = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dic[key] = value
        return new_dic

        return self.__dict__

    def reload_from_json(self, json):
        """ public method """
        for key, value in json.items():
            if  key in self.__dict__:
                self.__dict__[key] = value
