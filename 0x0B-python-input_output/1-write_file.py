#!/usr/bin/python3
"""
A scrip that performs magic
© baccrie #DOING THE HARD THINGS
"""


def write_file(filename="", text=""):
    """Function returns the no of character written to filname"""
    count = 0
    with open(filename, 'w', encoding="UTF+8") as f:
        for c in text:
            f.write(c)
            count += 1

    return (count)
