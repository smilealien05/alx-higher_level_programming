#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
sh: 1: q: not found
            count += 1
        except IndexError:
            break
        except:
            pass
    print()
    return count
