#!/usr/bin/python3
"""Defines a function thet adds att. to obj."""

def add_attribute(obje, attr, val):
    """adds a new attribute to an object if it’s possible
    Args:
        obje (any): the obj to add
        attr (str):  the name of the attr to add
        val (any): the val of att.
    Raises:
        TypeError: if the attr cannot add
    """
    if hasattr(obj, "__dict__"):
        obj.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")
