#!/usr/bin/python3
"""
contains a class MyInt
"""

class MyInt(int):
    """MyInt is a rebel of int."""
    #def __new__(cls, *args, **kwargs):
    #    """create a new instance of the class"""
    #    return super(MyInt, cls).__new(cls, *args, **kwargs)

    def __eq__(self, other):
        """Reverse != to =="""
        return int(self) != other
    def __ne__(self, other):
        """Reverse == to !="""
        return int(self) == other
