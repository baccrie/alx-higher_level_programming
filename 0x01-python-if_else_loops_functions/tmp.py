#!/usr/bin/env python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    rem = number * (-1)
    rem = rem % 10
    rem = rem * (-1)
else:
    rem = number % 10

print(f"The number is {number} and last num is {rem}")
