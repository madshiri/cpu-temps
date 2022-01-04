#! /usr/bin/env python3

"""
This module computes global linear least squares approximation using interpolate() function.
"""

import numpy as np
import matrix_solver


def approximate(x_values, y_values):
    """
    This function computes global least square approximation on given X and Y values

    Args:
        x_values: a numpy array of size n*1 which contains times as X values
        y_values: a numpy array of size n*1 which contains times as Y values

    Returns:
        a dictionary containing coefficients of approximated function
        {'xi': , 'xi+1': , 'yi': ,'c0': , 'c1': , 'type':}
    """
    x = np.reshape(x_values, (len(x_values), 1))
    x = np.insert(x, 0, [1] * len(x_values), axis=1)
    y = np.reshape(y_values, (len(y_values), 1))
    xt = x.T
    c0, c1 = matrix_solver.solve(x, xt, y)
    data = {'xi': x_values[0],
            'xi+1': x_values[-1],
            'yi': 'y',
            'coeffs': [c0, c1],
            'type': 'least_squares'}

    return data