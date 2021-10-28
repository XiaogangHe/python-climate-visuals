# What is SciPy?
```{margin} Source
from the SciPy [website](https://docs.scipy.org/doc/scipy/reference/tutorial/general.html)
```

SciPy is a collection of mathematical algorithms and convenience functions built on the NumPy extension of Python. It adds significant power to the interactive Python session by providing the user with high-level commands and classes for manipulating and visualizing data. With SciPy, an interactive Python session becomes a data-processing and system-prototyping environment rivaling systems, such as MATLAB, IDL, Octave, R-Lab, and SciLab.

```{admonition} SciPy capabilities
The capabilities of SciPy are defined by its sub-packages:
* `scipy.special`: includes the definition of numerous <u>special functions of mathematical physics</u> (including airy, elliptic, bessel, gamma, beta, hypergeometric, parabolic cylinder, mathieu, spheroidal wave, struve, and kelvin);
* `scipy.integrate`: provides several <u>integration techniques</u> including an ordinary differential equation integrator;
* `scipy.optimize`: provides functions for minimizing (or maximizing) <u>objective functions</u>, <u>solvers</u> for nonlinear problems, linear programing, constrained and nonlinear least-squares, root finding, and curve fitting;
* `scipy.interpolate`: provides functions for 1-D and 2-D <u>interpolation</u> and even a simple interface for N-dimensions interpolation;
* `scipy.fft`: provides numerical computing of Fast <u>Fourier Transform</u>;
* `scipy.signal`: contains some <u>filtering functions</u>, a limited set of filter design tools, and a few B-spline interpolation algorithms for 1- and 2-D data;
* `scipy.linalg`: privides faster and more <u>linear algebra</u> operations than `numpy.linalg`;
* `scipy.spatial`: can compute triangulations, Voronoi diagrams and convex hulls of a set of points, and also implements kd-tree for quick nearest-neighbor lookup;
* `scipy.stats`: contains a large number of <u>probability distributions</u>, summary and frequency <u>statistics</u>, correlation functions and statistical tests, masked statistics, kernel density estimation, quasi-Monte Carlo functionality;
* `scipy.ndimage`: provides a number of general <u>image processing and analysis functions</u> that are designed to operate with arrays of arbitrary dimensionality;
* `scipy.io`: provides <u>file inputs and outputs</u> beyond `numpy` for MATLAB, IDL, Matrix Market, WAV, arff and netcdf files.
```
