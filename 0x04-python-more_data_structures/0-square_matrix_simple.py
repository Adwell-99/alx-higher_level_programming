#!/usr/bin/python3

def square_matrix_alternative(matrix=[]):
    # Check if the matrix is empty
    if not matrix:
        return []

    # Create a new matrix with squared elements using map and lambda
    new_matrix = list(map(lambda row: list(map(lambda x: x**2, row)), matrix))

    return new_matrix

