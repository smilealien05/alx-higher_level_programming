#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = 0
if number < 0:
    n = -1 * number
    print(f"Last digit of {number} is -{n % 10} and ", end="")
else:
    print(f"Last digit of {number} is {number % 10} and ", end="")
if number < 0:
    print("is less than 6 and not 0")
elif number % 10 > 5:
    print("is greater than 5")
elif number % 10 == 0:
    print("is 0")
else:
    print("is less than 6 and not 0")
