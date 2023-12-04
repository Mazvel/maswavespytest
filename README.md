# MASWavesPy

MASWavesPy is a Python package for processing and inverting MASW data, developed at the Faculty of Civil and Environmental Engineering, University of Iceland. 

## Installation

`pip install maswavespy`

Wheels for Windows, Linux and Mac distributions can also be downloaded from [pypi](https://test.pypi.org/project/maswavespytest/#files).

We recommend to install the MASWavesPy package into an isolated Python environment. If using Anaconda, create a virtual environment using [conda](https://docs.conda.io/projects/conda/en/latest/commands/create.html). Alternatively, [virtualenv](https://docs.python.org/3/library/venv.html) can be used to install this package into an isolated Python environment. [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) is a tool to simplify the creation and management of local virtualenvs.

The use of a Python IDE (Integrated Development Environment) is strongly recommended for using MASWavesPy (as opposed to running commands in the Windows terminal/cmd environment). 

MASWavesPy is developed using the [Anaconda distribution](https://www.anaconda.com/). Hence Anaconda and the Spyder IDE (included with Anaconda) are recommended for running the Quick Start guide below. 

## Requirements

To build the package on Windows you need Microsoft C++ Build Tools. You can download an installer from Microsoft at this [link](https://visualstudio.microsoft.com/visual-cpp-build-tools/). Otherwise you will see an error:
```
error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
```
For more information you can view this Stackoverflow [answer](error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/)

This is required because the package uses [Cython](https://cython.org/) for some of its calculations.

## Quick Start (for Windows)

### Installation and setup

1. (If required) Download and install [Anaconda](https://www.anaconda.com/download).
2. (If required) Install [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/). The Microsoft C++ Build Tools are required for building the package on Windows.
3. (Optional, recommended) Create a virtual environment to install the package into an isolated Python environment. A brief guide is provided below.
   - Start Anaconda Prompt from the Start menu.
   - Verify that `conda` is installed in your path by typing `conda -V`
   - Navigate to the `anaconda3` directory.
   - Make sure that the newest version of `conda` is installed. Update conda by typing `conda update conda`.
   - Navigate back to the previous folder.
   - Get your python version (3.x.yy) by typing `python -V`.
   - Set up a virtual environment (here named `testenv`) by typing `conda create --name testenv python=3.x` (where 3.x is replaced by the python version that you have/want to use).
   - Activate the virtual environment by typing `conda activate testenv`. To see a list of available environments, type `conda info --envs`.
   - Install [spyder](https://www.spyder-ide.org/) into the virtual environment by typing `conda install spyder`.

### Install MASWavesPy through Anaconda Prompt. 

The package is installed using [pip](https://pip.pypa.io/en/stable/).
1. (If required) Start Anaconda Prompt.
2. Type `pip install maswavespy` to install the package.
3. Check if the package has been successfully installed by inspecting the last lines that are displayed in the Anaconda Prompt console.

### Test MASWavesPy

1. Download the contents of the [examples](https://github.com/Mazvel/maswavespytest/tree/main/examples) directory. Four example files to test different parts/commands of the MASWavesPy package are provided. The example files use data from the [examples/Data](https://github.com/Mazvel/maswavespytest/tree/main/examples/Data) directory. Further information is provided in each file. 
2. Launch Spyder (testenv) from the Start menu (i.e., Spyder (name of your virtual environment)).
   - Please note that all four example files are written to be run one cell at a time using the keyboard shortcut (Ctrl+Enter), Run > Run cell, or the Run cell button in the toolbar.
3. Open `MASWavesPy_Dispersion_test1.py` to test the basic methods of the `maswavespy.wavefield` and `maswavespy.dispersion` modules using a single data file.
4. Open `MASWavesPy_Dispersion_test2.py` to test the methods of the `maswavespy.wavefield` and `maswavespy.dispersion` modules using a `Dataset` object.
5. Open `MASWavesPy_Combination_test.py` to test the `maswavespy.combination` module.
6. Open `MASWavesPy_Inversion_test.py` to test the `maswavespy.inversion` module.

### Deactivate the virtual environment (if a virtual environment has been created)

1. (If required) Start Anaconda Prompt.
2. Close the virtual environment `testenv` by typing `conda deactivate`.
3. If required, the virtual environment `testenv` can be deleted with the following command `conda remove --name testenv -all`.

## Known Issues

### Matplotlib should use TkAgg on Mac

MaswavesPy depends on matplotlib. If you are on mac you need to ensure matplotlib uses `TkAgg`. Below is a workaround that are used in our examples.

```
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")
```

### Tkinter not found on Mac 

On mac you might run into `ModuleNotFoundError: No module named '_tkinter'` error, even after successfully installing `maswavespy` that has [Tkinter](https://docs.python.org/3/library/tkinter.html) as one of its listed dependencies. This might be because your python3 installation did not have Tkinter correctly set up. Below is an example of how it can be installed with brew.

`brew install python-tk`
