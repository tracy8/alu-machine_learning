#!/usr/bin/env python3
def np_slice(matrix, axes={}):
    """Slices a matrix along specific axes

    Args:
        matrix (numpy.ndarray): matrix to slice
        axes (dict): dictionary where the key is an axis to slice along and
                     the value is a tuple representing the slice to make along
                     that axis

    Returns:
        numpy.ndarray: the sliced matrix
    """
    slices = []
    for i in range(matrix.ndim):
        if i in axes:
            slices.append(slice(*axes[i]))
        else:
            slices.append(slice(None))
    return matrix[tuple(slices)]