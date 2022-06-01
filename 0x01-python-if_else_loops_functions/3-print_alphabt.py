#!/usr/bin/python3
# Printing a to z using ascii codes a to z represent 97 to 122

asciiAlpha = 96

while asciiAlpha <= 122:
    asciiAlpha += 1
    if asciiAlpha == 101 or asciiAlpha == 113:
        continue
    print("{:c}".format(asciiAlpha), end='')
