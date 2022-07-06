#!/usr/bin/python3
import random
number = random.randint(1000,  10000)
div = number / 10
div = int(div) * 10
rem = number - div

if (rem < 0):
    print("{} has {} remainder".format(number, rem))
elif (rem > 0):
    print("{} has {} remainder".format(number, rem))

