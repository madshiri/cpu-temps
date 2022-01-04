#! /usr/bin/env python3

"""
This module computes natural cubic spline interpolation using interpolate() function.
"""


def interpolate(x_values, y_values):
    """
    This function computes natural cubic spline interpolation on given X and Y values

    Args:
        x_values: a numpy array of size n*1 which contains times as X values
        y_values: a numpy array of size n*1 which contains times as Y values

    Returns:
        dictionaries containing coefficients of approximated functions
        {'xi': , 'xi+1': , 'yi': ,'c0': , 'c1': , 'type':}
    """
    data = []
    n = len(x_values) - 1
    h = [x_values[i+1] - x_values[i] for i in range(n)]
    df = [(y_values[i+1] - y_values[i]) / h[i] for i in range(n)]
    m = [0] + [3*(df[i+1] - df[i]) / (h[i+1] + h[i]) for i in range(n-1)] + [0]
    a = [(m[i+1] - m[i]) / (6*h[i]) for i in range(n)]
    b = [m[i]/2 for i in range(n)]
    c = [df[i] - h[i] * (m[i+1] + 2*m[i]) / 6 for i in range(n)]
    d = [y_values[i] for i in range(n)]

    for i in range(n):
        data.append({'xi': x_values[i],
                     'xi+1': x_values[i+1],
                     'yi': f'y{i}',
                     'coeffs': [a[i], b[i], c[i], d[i]],
                     'type': 'cubic_spline_interpolation'})

    return data