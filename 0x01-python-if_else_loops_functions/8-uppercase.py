#!/usr/bin/python3
def uppercase(str):
    j = 0
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            print("{}".format(chr(ord(i)-32)), end="")
        else:
            print("{}".format(i), end="")
