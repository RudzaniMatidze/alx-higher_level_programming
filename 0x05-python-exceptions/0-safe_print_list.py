#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
        a = 0
        count = 0
        for a in range(0, x):
            try:
                print("{}".format(my_list[a]), end="")
                count += 1
            except:
                continue
            print()
            return count
