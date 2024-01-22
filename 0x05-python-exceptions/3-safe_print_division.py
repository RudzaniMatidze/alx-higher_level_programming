#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        count = a / b
    except (TypeError, ZeroDivisionError):
        count = None
    finally:
        print("Inside result: {}".format(div))
    return (count)
