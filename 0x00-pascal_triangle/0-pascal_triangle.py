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
