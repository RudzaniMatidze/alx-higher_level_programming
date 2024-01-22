#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        s_print = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
        print()
        return s_print
    except IndexError:
        print()
        return s_print
