#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for r in range(len(new_list)):
        if new_list[r] == search:
            new_list[r] = replace
    return new_list
