#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for a in range(x):
            value = my_list[a]
            if type(value) is int:
                print("{:d}".format(value), end="")
                count += 1
        print()
        return count
    except IndexError:
        print()
        return count
