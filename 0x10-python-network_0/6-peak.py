#!/usr/bin/python3
"""Find a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Find a peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None

    if len(list_of_integers) <= 2:
        return max(list_of_integers)

    if list_of_integers[0] > list_of_integers[1]:
        return find_peak(list_of_integers[1:])
    else:
        return find_peak(list_of_integers[2:])
