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

    def __del__(self):
        print("StackIter deleted")

    """
    class methods
    """

    def __init__(self, s):
        self.__stk = self.s

    def __del__(self):
        print("StackIter deleted")

    def first(self):
        self.__index = 0

    def next(self):
        self.__index += 1

    def isDone(self):
        self.__index = 0


createIterator = StackIter()

"""
    overloaded '==' operator
"""


def __eq__(self, l, r):
    itl = StackIter();
    itr = StackIter();
    itl = l.createIterator()
    itr = r.createIterator()

    eval = (itl.first(), itl.first(), itl.isDone(), itl.next(), itr.next())
    for x in eval:
        if itl.currentItem() != itr.currentItem():
            break
    ans = (itl.isDone() & itr.isDone())
    del itl
    del itr
    return ans
