#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    max_value = my_list[0]
    for numb in my_list:
        if numb > max_value:
            max_value = numb

    return max_value
