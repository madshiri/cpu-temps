CPU Temperatures Project

# Getting Started

**Language:** Python 3.9

# Requirements

> This code makes use of the `f"..."` or [f-string
> syntax](https://www.python.org/dev/peps/pep-0498/). This syntax was
introduced in Python 3.6.\
> Numpy v1.21.2 is used as an external library.\
> Modules least_square_approximation, linear_interpolation and 
cubic_spline_interpolation are dependencies for cpu_temps_driver program.\
> Module matrix_solver is a dependency for least_square_approximation module.

# Compilation & Execution Instructions

If run without command line arguments, using

```
python ./cpu_temps_driver.py
```

the following usage message will be displayed.

```
Usage: python ./cpu_temps_driver.py PATH_TO_INPUT_FILE
```

If run on one dataset in input folder using

```
python ./cpu_temps_driver.py input/sensors-2018.12.26.txt
```

four files in output folder *simliar* to

```
output/sensors-2018-core-0.txt
output/sensors-2018-core-1.txt
output/sensors-2018-core-2.txt
output/sensors-2018-core-3.txt
```

will be generated.

---
