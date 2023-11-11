# MaswavesPy

MaswavesPy is a Python package for processing and inverting MASW data. MASWaves (Multichannel Analysis of Surface Waves for assessing shear wave velocity profiles of soils) is an open source software, developed at the Faculty of Civil and Environmental Engineering, University of Iceland, for processing and analyzing multichannel surface wave records using MASW. 

## Installatilion

`pip install maswavespy`

Wheels for Windows, Linux and Mac distributions can also be downloaded from [pypi](https://test.pypi.org/project/maswavespytest/#files).

## Quick Start

In the [examples](https://github.com/Mazvel/maswavespytest/tree/main/examples) directory you can see some examples. It uses data from the [examples/Data](https://github.com/Mazvel/maswavespytest/tree/main/examples/Data) directory for the calculations.

## Known Issues

### Matplotlib shoulds use TkAgg on Mac

MaswavesPy depends on matplotlib. If you are on mac you need to ensure matplotlib uses `TkAgg`. Below is a workaround that are used in our examples.

```
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")
```

### Tkinter not found on Mac 

On mac you might run into `ModuleNotFoundError: No module named '_tkinter'` error, even after successfully installing `maswavespy` that has [Tkinter](https://docs.python.org/3/library/tkinter.html) as one of its listed dependencies. This might be because your python3 installation did not have Tkinter correctly set up. Below is an example of how it can be installed with brew.

`brew install python-tk`
