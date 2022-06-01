#!/usr/bin/python3
# Printing a to z using ascii codes a to z represent 97 to 122

asciiAlpha = 97

while asciiAlpha <= 122:
    print("{:c}".format(asciiAlpha), end='')
    asciiAlpha += 1
