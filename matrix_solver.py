#! /usr/bin/env python3

"""
This module is a collection of functions to solve systems of equations as matrices using gaussian elimination algorithm
for given matrix X, XT and Y with calling solve() function.
"""

import numpy as np


def multiply(lhs, rhs):
    """
    This function takes two matrices and does the multiplication

    Args:
        lhs: left matrix of size n*m
        rhs: right matrix of size m*p

    Returns:
        a matrix of size n*p
    """
    n = lhs.shape[0]
    m = lhs.shape[1]
    p = rhs.shape[1]

    result = np.zeros((n, p))
    for i in range(n):
        for j in range(p):
            for k in range(m):
                result[i][j] += lhs[i][k] * rhs[k][j]

    return result


def solve(x, xt, y):
    """
    This function takes three matrices that form XTX|XTY(Ax=b) and solve the equation to obtain the vector b

    Args:
        x: a matrix of size n*m
        xt: transpose of x which is of size m*n
        y: matrix of size n*1

    Returns:
        a vector b of type float with size of m
    """
    xtx = multiply(xt, x)
    xty = multiply(xt, y)
    aug_mat = np.concatenate((xtx, xty), axis=1)
    num_rows = aug_mat.shape[0]
    num_cols = aug_mat.shape[1]

    for i in range(num_rows):
        idx = find_largest_row_by_col(aug_mat, i)
        swap(aug_mat, i, idx)
        scale(aug_mat, i, num_cols, aug_mat[i][i])
        eliminate(aug_mat, i, num_cols, num_rows)
    back_solve(aug_mat, num_cols, num_rows)

    return aug_mat[:, -1]


def find_largest_row_by_col(mat, col_idx):
    """
    This function finds the largest row in a given column

    Args:
        mat: a matrix
        col_idx: the index of column 

    Returns:
        index of maximum value in the given column
    """
    max_value = max(mat[col_idx:, col_idx])
    max_idx = np.where(mat[:, col_idx] == max_value)[0][0]
    return max_idx


def swap(mat, row1_idx, row2_idx):
    """
    This function swaps two rows in a matrix with given row indices

    Args:
        mat: a matrix
        row1_idx: a row index of the matrix
        row2_idx: a row index of the matrix
    """
    mat[[row1_idx, row2_idx]] = mat[[row2_idx, row1_idx]]


def scale(mat, row_idx, num_cols, s):
    """
    This function scale a row of a matrix with multiplying the scale value to the row elements

    Args:
        mat: a matrix
        row_idx: a row index of the matrix
        num_cols: number of columns of the matrix
        s: scale value
    """
    for j in range(num_cols):
        mat[row_idx][j] /= s


def eliminate(mat, row_idx, num_cols, num_rows):
    """
    This function performs gaussian elimination on a matrix with a given row index

    Args:
        mat: a matrix
        row_idx: a row index of the matrix
        num_cols: number of columns of the matrix
        num_rows: number of rows of the matrix
    """
    for i in range(row_idx+1, num_rows):
        s = mat[i][row_idx]
        for j in range(row_idx, num_cols):
            mat[i][j] -= s * mat[row_idx][j]


def back_solve(mat, num_cols, num_rows):
    """
    This function performs backsolve on a given matrix

    Args:
        mat: a matrix
        num_cols: number of columns of the matrix
        num_rows: number of rows of the matrix
    """
    aug_col_idx = num_cols - 1
    for i in range(num_rows-1, 0, -1):
        for j in range(i-1, -1, -1):
            s = mat[j][i]
            mat[j][i] -= s * mat[i][i]
            mat[j][aug_col_idx] -= s * mat[i][aug_col_idx]