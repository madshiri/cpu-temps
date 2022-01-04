#! /usr/bin/env python3

"""
This program computes global linear least squares approximation, linear piecewise interpolation and natural cubic spline
interpolation for the CPU temperatures cpu_temps_project. It takes CPU temperatures data and process it, then it
calculates approximated functions per core and output them to files.
"""

import os
import sys
import numpy as np
import linear_interpolation
import cubic_spline_interpolation
import least_square_approximation

from parse_temps import parse_raw_temps


def main(input_temps):
    """
    This main function serves as the driver for the CPU temperatures cpu_temps_project. Such functions
    are not required in Python. However, we want to prevent unnecessary module
    level (i.e., global) variables.
    """
    steps = []
    temps = []

    # read input data
    with open(input_temps, 'r') as temps_file:
        for temps_as_floats in parse_raw_temps(temps_file):
            steps.append(temps_as_floats[0])
            temps.append(temps_as_floats[1])

    # data to arrays
    steps_arr = np.asarray(steps)
    temps_arr = np.asarray(temps)

    cores = temps_arr.shape[1]
    basename = input_temps.split('/')[-1].split('.txt')[0]

    if not os.path.isdir('output'):
        os.mkdir('output')

    # iterate over each core
    for core in range(cores):
        file = open(f'output/{basename}-core-{core}.txt', 'w')

        # linear interpolation
        lis = linear_interpolation.interpolate(steps_arr, temps_arr[:, core])
        for li in lis:
            write_to_file(file, li)

        # cubic spline interpolation
        csis = cubic_spline_interpolation.interpolate(steps_arr, temps_arr[:, core])
        for csi in csis:
            write_to_file(file, csi)

        # least square approximation
        ls = least_square_approximation.approximate(steps_arr, temps_arr[:, core])
        write_to_file(file, ls)

        file.close()


def write_to_file(file, data):
    """
    This function write a given dictionary containing variables and values associated with a function to a given file
    Args:
        file: a file which has been opened
        data: a dictionary {'xi': , 'xi+1': , 'yi': ,'coeffs': , 'type':}
    """
    function = ''
    i = 0
    for coeff in data['coeffs']:
        if i == 0:
            x_degree = ''
        elif i == 1:
            x_degree = 'x'
        else:
            x_degree = f'x^{i}'

        function += f'{"{:.4f}".format(coeff)}{x_degree} + '

        i += 1

    line = f'{data["xi"]} <= x < {data["xi+1"]}; ' \
           f'{data["yi"]} = {function[:-3]}; ' \
           f'{data["type"]}\n'

    file.write(line)


if __name__ == "__main__":
    # check input argument
    if len(sys.argv) != 2:
        print('Usage: ./cpu_temps_driver.py PATH_TO_INPUT_FILE')
        sys.exit(1)
    main(sys.argv[1])
