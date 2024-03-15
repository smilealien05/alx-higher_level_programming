#!/usr/bin/python3
def no_c(my_string):
    istr = my_string[:]
    while 'c' in istr or 'C' in istr:
        if 'c' in istr:
            istr = istr[:istr.index('c')] + istr[istr.index('c') + 1:]
        if 'C' in istr:
            istr = istr[:istr.index('C')] + istr[istr.index('C') + 1:]
    return istr
