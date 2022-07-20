#!/usr/bin/python3
"""A magical module"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Alx sucks"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns wahala"""
        new = self.__dict__
        return (new)
