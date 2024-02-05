#!/usr/bin/python3
"""
Class Called BaseGeometry
"""


class BaseGeometry:
    """A class called BaseGeometry"""

    def area(self):
        """A function that Raise an Error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check if Value is a positive Number"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

