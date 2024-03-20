#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = set()
    for elem in set_1:
        if elem not in set_2:
            common.add(elem)
   for el in set_2:
        if el not in set_1:
            common.add(el)
    return common
