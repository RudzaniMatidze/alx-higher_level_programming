#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 idx >= len(my_list):
        return my_list

    new_list = []
    for a in range(len(my_list)):
        if a != idx:
            new_list.append(my_list[a])

    return new_list
