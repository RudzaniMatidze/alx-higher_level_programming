#!/usr/bin/python3
"""Define a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    from anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
