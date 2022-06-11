#!/usr/bin/python3
import math
import random
number = random.randint(-10000, 10000)
rem = int(math.fmod(number, 10))
if (rem > 5):
    print(f"Last digit of {number:d} is {rem:d} and is greater than 5")
elif (rem == 0):
    print(f"Last digit of {number:d} is {rem:d} and is {rem:d}")
else:
    print(f"Last digit of {number:d} is {rem:d} and is less than\
 6 and not 0")
