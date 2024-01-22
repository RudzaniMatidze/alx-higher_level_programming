#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for a in range(x):
            print("{}".format(my_list[a]), end="")
            count += 1
            print()
            return count
        except IndexError:
            print()
            return count
