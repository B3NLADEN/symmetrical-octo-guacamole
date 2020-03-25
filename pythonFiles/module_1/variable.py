#!/usr/bin/python


class MyClass:
    """A simple example class"""

    i = 23


newM = MyClass()
num1 = newM.i
print num1
newM.i = 24
print newM.i
print newM.__doc__

