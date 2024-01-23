#!/usr/bin/python3

""" Node - is defining a singly linked """


class Node:
    """ this is a Node """
    def __init__(self, data, next_node=None):
        """ constructor """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ data instance """
        return self.__data

    @data.setter
    def data(self, value):
        """ set new ddata """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ next_node instance """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ set new next node """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


""" singly linked - is defining a singly linked """


class SinglyLinkedList:
    """ singly for the best """
    def __init__(self):
        """ init new head """
        self.__head = None

    def sorted_insert(self, value):
        """ insert new node """
        new_node = Node(value)

        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and\
                    current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """ print data """
        result = ""
        current = self.__head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
