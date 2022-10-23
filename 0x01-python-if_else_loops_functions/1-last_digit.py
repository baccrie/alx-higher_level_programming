#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    rem = (number * (-1))
    rem = rem - ((rem // 10) * 10)
    rem = rem * (-1)
else:
    rem = number % 10
if rem > 5:
    print(f"Last digit of {number:d} is {rem:d} and is greater than 5")
elif  rem < 6 and rem != 0:
    print(f"Last digit of {number:d} is {rem:d} and is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is 0 and is 0")
