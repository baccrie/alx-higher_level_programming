#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
# The import math above allows me to use the fmod methos below
# The variable rem gets the non absolute remainder of the modulus
rem = int(math.fmod(number, 10))
if (rem > 5):
    print(f"Last digit of {number} is {rem} and is greater than 5")
elif (rem == 0):
    print(f"Last digit of {number} is {rem} and is 0")
elif ((rem < 6) & (rem != 0)):
    print(f"Last digit of {number} is {rem}\
 and is less than 6 and not 0")
