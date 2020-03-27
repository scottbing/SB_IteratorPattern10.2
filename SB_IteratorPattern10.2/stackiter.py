from stack import *


class StackIter(object):
    """
    class variables
    """
    __stk = Stack()
    __index = None

    """
    class constructor
    """
    def __init__(self):
        pass

    """
    class methods
    """
    def __init__(self, s):
        self.__stk = self.s

    def first(self):
        self.__index = 0

    def next(self):
        self.__index += 1

    def isDone(self):
        self.__index = 0


createIterator = StackIter()
