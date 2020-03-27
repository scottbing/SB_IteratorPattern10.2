class Stack():
    """
    class variables
    """
    __items = []
    __sp = None

    def __init__(self):
        self.__sp = - 1

    def push(self, item):
        self.__sp += 1
        self.__items[self.__sp] = item

    def pop(self):
        self.__sp -= 1
        return self.__items[self.__sp]

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []
