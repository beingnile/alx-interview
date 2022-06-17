#!/usr/bin/python3

"""Defines a function pascal_triangle that
returns a representation of the Pascal's triangle
"""


def pascal_triangle(n):
    """
    Args:
        n (int): The number of rows in the triangle whereby n >= 1

    Returns:
        list: a list of lists of integers representing the
        Pascal's triangle of n.
    """
    res = []
    if n <= 0:
        return(res)

    res = [[1]]

    for i in range(n - 1):
        row_above = [0] + res[i] + [0]
        row = []
        for j in range(len(row_above) - 1):
            row.append(row_above[j] + row_above[j + 1])
        res.append(row)
    return res
