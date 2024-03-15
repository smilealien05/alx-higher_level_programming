#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        llist = my_list[:]
        return llist
    llist = my_list[:]
    llist[idx] = element
    return llist
