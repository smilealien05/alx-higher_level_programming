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
    if not hasattr(obje, "__dir__"):
        raise TypeError("can't add new attribute")
    setattr(obje, attr, val)
