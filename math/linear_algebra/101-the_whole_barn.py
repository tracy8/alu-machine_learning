#!/usr/bin/env python3
def add_matrices(mat1, mat2):
    """
    Adds two matrices of any dimension.

    Args:
        mat1: First matrix (list of lists or nested lists of ints/floats)
        mat2: Second matrix (same shape as mat1)

    Returns:
        A new matrix representing the element-wise sum,
        or None if shapes do not match.
    """
    def shape(matrix):
        s = []
        while isinstance(matrix, list):
            s.append(len(matrix))
            matrix = matrix[0]
        return s

    if shape(mat1) != shape(mat2):
        return None

    if not isinstance(mat1[0], list):
        return [mat1[i] + mat2[i] for i in range(len(mat1))]

    return [add_matrices(mat1[i], mat2[i]) for i in range(len(mat1))]