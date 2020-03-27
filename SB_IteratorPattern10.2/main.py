from Stack  import *
from StackIter import *

if __name__ == '__main__':

    s1 = Stack()
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
