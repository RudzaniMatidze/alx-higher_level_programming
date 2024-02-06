#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returnss a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangle) != n:
        tri = triangles[-1]
        tmp = [1]
        for a in range(len(tri) - 1):
            tmp.append(tri[a] + tri[a + 1])
            triangles.append(tmp)
        return triangles
