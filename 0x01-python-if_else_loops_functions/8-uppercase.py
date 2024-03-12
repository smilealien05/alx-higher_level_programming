#!/usr/bin/python3
def uppercase(str):
    j = 0
    for i in str:
        print("{}".format(chr(ord(i)-32)) if ord('a') <= ord(i) <= ord('z') else "{}".format(i), end="")
    print()
