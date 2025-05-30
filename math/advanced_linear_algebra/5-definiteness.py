#!/usr/bin/env python3
"""
Module for calculating definiteness of a matrix
"""


import numpy as np


def definiteness(matrix):
    """
    Determines the definiteness of a matrix.

    Parameters:
    matrix (numpy.ndarray): A square matrix to check.

    Returns:
    str: A string describing the definiteness of the matrix,
    or None if the matrix is invalid.

    Raises:
    TypeError: If the input is not a numpy.ndarray.
    """

    # Check if matrix is a numpy ndarray
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    # Debugging: Print the matrix type and shape for validation
    print(f"Matrix type: {type(matrix)}")
    print(f"Matrix shape: {matrix.shape}")

    # Check if the matrix is square and valid
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        print("Matrix is not square or has invalid dimensions.")
        return None

    # Check if the matrix is symmetric
    if not np.allclose(matrix, matrix.T):
        print("Matrix is not symmetric.")
        return None

    # Calculate the eigenvalues
    eigenvalues = np.linalg.eigvals(matrix)

    # Debugging: Print the eigenvalues for inspection
    print(f"Eigenvalues: {eigenvalues}")

    # Check the eigenvalues to determine the definiteness
    if np.all(eigenvalues > 0):
        return "Positive definite"
    elif np.all(eigenvalues >= 0):
        return "Positive semi-definite"
    elif np.all(eigenvalues < 0):
        return "Negative definite"
    elif np.all(eigenvalues <= 0):
        return "Negative semi-definite"
    else:
        return "Indefinite"
