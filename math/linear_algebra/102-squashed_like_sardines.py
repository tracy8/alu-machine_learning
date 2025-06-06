#!/usr/bin/env python3
def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.

    Args:
        mat1: First matrix (list of lists or nested lists of ints/floats)
        mat2: Second matrix (same shape except in the concatenation axis)
        axis: Axis along which to concatenate

    Returns:
        A new matrix representing the concatenation,
        or None if shapes are not compatible.
    """
    def shape(matrix):
        s = []
        while isinstance(matrix, list):
            s.append(len(matrix))
            matrix = matrix[0]
        return s

    def check_shapes(s1, s2, axis):
        if len(s1) != len(s2):
            return False
        for i in range(len(s1)):
            if i != axis and s1[i] != s2[i]:
                return False
        return True

    s1 = shape(mat1)
    s2 = shape(mat2)
    if not check_shapes(s1, s2, axis):
        return None

    if axis == 0:
        return mat1 + mat2

    return [cat_matrices(m1, m2, axis - 1) for m1, m2 in zip(mat1, mat2)]