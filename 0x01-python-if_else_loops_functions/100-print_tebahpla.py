#!/usr/bin/python3
for i in range(90, 64, -1):
    if i % 2 == 1:
        print(chr(i), end='')
    else:
        print(chr(i + 32), end='')
