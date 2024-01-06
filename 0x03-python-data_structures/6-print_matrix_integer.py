#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for a, number in enumerate(row):
            print("{:d}".format(number), end="")
            if a < len(row) - 1:
                print(" ", end="")
        print()
