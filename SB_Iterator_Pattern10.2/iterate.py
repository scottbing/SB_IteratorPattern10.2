class Stack(object):
    """
    class variables
    """
    items = []
    sp = None

    def __init__(self):
      self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


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


def createIterator():
    return object.__new__(StackIter)


"""
    overloaded '==' operator
"""


def __eq__(self, l, r):
    itl = StackIter()
    itr = StackIter()
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


if __name__ == '__main__':

    s1 = Stack()
    #for i in range(1, 5, 1):
    for i in range(5):
        s1.push(i)

    """
        s2-s5 same as s1
    """
    s2 = s1
    s3 = s1
    s4 = s1
    s5 = s1
    """
        test the stack operations
    """
    s3.pop()
    s5.pop()
    s4.push(2)
    s5.push(9)

    """
        Demonstrate overloaded operator
    """
    print("1 == 2", (s1 == s2))
    print("1 == 3", (s1 == s3))
    print("1 == 4", (s1 == s4))
    print("1 == 5", (s1 == s5))
