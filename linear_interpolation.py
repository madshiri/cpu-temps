#! /usr/bin/env python3

"""
This module computes linear piecewise interpolation using interpolate() function.
"""


def interpolate(x_values, y_values):
    """
    This function computes piecewise linear interpolation on given X and Y values

    Args:
        x_values: a numpy array of size n*1 which contains times as X values
        y_values: a numpy array of size n*1 which contains times as Y values

    Returns:
        dictionaries containing coefficients of approximated functions
        {'xi': , 'xi+1': , 'yi': ,'c0': , 'c1': , 'type':}
    """
    data = []
    for i in range(len(x_values) - 1):
        x = x_values[i:i + 2]
        y = y_values[i:i + 2]
        c1 = (y[1] - y[0]) / (x[1] - x[0])
        c0 = y[0] + (c1 * x[0])
        data.append({'xi': x_values[i],
                     'xi+1': x_values[i+1],
                     'yi': f'y{i}',
                     'coeffs': [c0, c1],
                     'type': 'linear_interpolation'})

    return data