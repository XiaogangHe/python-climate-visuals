# What is Xarray?
```{margin} Source
from the Xarray [website](http://xarray.pydata.org/en/stable/getting-started-guide/why-xarray.html)
```

xarray (formerly xray) is an open source project and Python package that makes working with labelled multi-dimensional arrays simple, efficient, and fun!

```{admonition} Xarray capabilities
* N-D labeled arrays: Xarray introduces labels in the form of dimensions, coordinates and attributes on top of raw NumPy-like arrays, which allows for a more intuitive, more concise, and less error-prone developer experience;
* Customized for NetCDF files:  It is particularly tailored to working with netCDF files, which were the source of xarray’s data model;
* Parallel computing with Dask: xarray integrates with Dask to support parallel computations and streaming computation on datasets that don’t fit into memory;
* Plotting: Labeled data enables expressive computations. These same labels can also be used to easily create informative plots;
* Integrates well with other libraries: Xarray leverage first-class external libraries for core features of xarray (e.g., NumPy for ndarrays, pandas for indexing, dask for parallel computing). Xarray expose internal abstractions to users, which facilitates extending xarray in various ways;
* Widely used: The dominant use-case for xarray is for the analysis of gridded datasets in the geosciences and physical sciences, and also is used in a variety of other domains, including finance, probabilistic programming, and genomics;
* A domain agnostic solution: Xarray focus on providing a flexible set of functionality related labeled multidimensional arrays, rather than solving particular problems. This facilitates collaboration between users with different needs, and helps us attract a broad community of contributers. Importantly, this retains flexibility, for use cases that don’t fit particularly well into existing frameworks.
```

