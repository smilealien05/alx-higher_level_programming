#!/usr/bin/python3
'''module for lockup method'''

def def lookup(obj):
    '''Looks up object attributes and methods.
    Args:
        obj (object) : the obj to list.
    Returns:
        list: the list of attributes.
    '''
    return dir(obj)
