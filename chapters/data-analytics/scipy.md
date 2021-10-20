# What is SciPy?
```{margin} Source
from the Pandas [website](https://docs.scipy.org/doc/scipy/reference/tutorial/general.html)
```

SciPy is a collection of mathematical algorithms and convenience functions built on the NumPy extension of Python. It adds significant power to the interactive Python session by providing the user with high-level commands and classes for manipulating and visualizing data. With SciPy, an interactive Python session becomes a data-processing and system-prototyping environment rivaling systems, such as MATLAB, IDL, Octave, R-Lab, and SciLab.

```{admonition} SciPy capabilities
The capabilities of SciPy are defined by its sub-packages:
* `scipy.special`: includes the definition of numerous special functions of mathematical physics (including airy, elliptic, bessel, gamma, beta, hypergeometric, parabolic cylinder, mathieu, spheroidal wave, struve, and kelvin);
* `scipy.integrate`: provides several integration techniques including an ordinary differential equation integrator;
* `scipy.optimize`: provides functions for minimizing (or maximizing) objective functions, solvers for nonlinear problems, linear programing, constrained and nonlinear least-squares, root finding, and curve fitting;
* `scipy.interpolate`: provides functions for 1-D and 2-D interpolation and even a simple interface for N-dimensions interpolation;
* `scipy.fft`: provides numerical computing of Fast Fourier Transform;
* `scipy.signal`: contains some filtering functions, a limited set of filter design tools, and a few B-spline interpolation algorithms for 1- and 2-D data;
* `scipy.linalg`: privides faster and more linear algebra operations than `numpy.linalg`;
* `scipy.spatial`: can compute triangulations, Voronoi diagrams and convex hulls of a set of points, and also implements kd-tree for quick nearest-neighbor lookup;
* `scipy.stats`: contains a large number of probability distributions, summary and frequency statistics, correlation functions and statistical tests, masked statistics, kernel density estimation, quasi-Monte Carlo functionality;
* `scipy.ndimage`: provides a number of general image processing and analysis functions that are designed to operate with arrays of arbitrary dimensionality;
* `scipy.io`: provides file inputs and outputs beyond `numpy` for MATLAB, IDL, Matrix Market, WAV, arff and netcdf files.
```
