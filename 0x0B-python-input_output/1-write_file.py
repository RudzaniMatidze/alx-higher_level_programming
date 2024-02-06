#!/usr/bin/python3
"""Defines a file-writing function. """


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (ste): The text to write the file.
    Returns"
        The numbet of characters written.
    """
    with open(filename, "w", encoding="utf8") as f:
    return f.write(text)
