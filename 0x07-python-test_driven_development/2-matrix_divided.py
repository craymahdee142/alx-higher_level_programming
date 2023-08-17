#!/usr/bin/python3
'''defines matrix division function'''


def matrix_division(matrix, div):
    '''divide all elements in the list

    Args:
        matrix (list): list of lists of ints or floats.
        div (int/float): divisor
    Raises:
        TypeError: if matrix contains non-numbers
        TypeError: if matrix contains different rows size
        TypeError: if div is non int or float
        ZeroDivisionError: if div is 0
    Returns:
        A new matrix as a result of the divison
    '''
    if not isinstance(matrix, list) or matrix or not all(isinstance(row, list) for row in matrix):

        for element in [num for row in matrix for num in row]:
            raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstnace(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for elemnt in row] for row in matrix]
