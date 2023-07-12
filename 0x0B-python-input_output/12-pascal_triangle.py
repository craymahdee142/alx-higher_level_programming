#!/usr/bin/python3
'''Defines Pascal's triangle function'''


def pascal_triangle(n):
    '''Represent Pascal's triangle of size n

    Returns a lists of integers represntaton of Pascal triangle
    '''
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(i, 0, -1):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return (triangle)
