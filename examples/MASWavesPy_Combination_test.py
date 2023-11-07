# -*- coding: utf-8 -*-
"""
Test MASWavesPy Combination

This example covers the use of CombineDCs objects to:
- Initialize a CombineDCs object.
- View the experimental DCs and evaluate the variation in DCs estimates
  with frequency in terms of the coefficient of variation (COV=std/mean).
- Evaluate a compusite dispersion curve for the dataset following the 
  procedure described in Olafsdottir et al. (2018).
- Resample composite experimental dispersion curves.


The following packages are required:
- numpy
- matplotlib
- scipy
- csv (to run this example)


References
----------
Dispersion curve combination
 - Olafsdottir, E.A., Bessason, B. and Erlingsson, S. (2018b). Combination of 
   dispersion curves from MASW measurements. Soil Dynamics and Earthquake 
   Engineering 113: 473–487. https://doi.org/10.1016/j.soildyn.2018.05.025

"""
from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")

from maswavespy import combination

# Import picked dispersion curves (stored as .txt files in the folder Data)
import numpy as np

# Path to sample data
filename_c = 'Data/Oysand_c_list.txt' # phase velocity
filename_f = 'Data/Oysand_f_list.txt' # frequency

with open(filename_c, 'r') as file_c:
    c_vec = [np.array([float(value) for value in line.split()]) for line in file_c]

with open(filename_f, 'r') as file_f:
    f_vec = [np.array([float(value) for value in line.split()]) for line in file_f]

del file_c, file_f
#%%
# Initialize a CombineDCs object
site = 'Oysand'
profile = 'P1'
c_TestSite = combination.CombineDCs(site, profile, f_vec, c_vec)

# Please note that when working with datasets, a CombineDCs object for the dataset
# can be initialized in a more convenient manner (see Examples/MASWavesPy_Dispersion_test2)

#%%
# View the imported experimental DCs and evaluate the variation in DCs estimates
# with frequency in terms of the coefficient of variation.
binwidth = 0.1 # Width of frequency bins for computation of COV values
c_TestSite.dc_cov()
c_TestSite.plot_dc_cov()

#%%
# Evaluate a compusite dispersion curve for the dataset following the 
# procedure described in Olafsdottir et al. (2018). The elementary dispersion
# curve data points are grouped within log-a spaced wavelength bands. The 
# arithmetic mean of the dispersion curve phase velocity values within each 
# wavelength band is used as a point estimate of the phase velocity of 
# Rayleigh wave components within the given wavelength range.
# The returned upper/lower boundary curves correspond to plus/minus no_std 
# standard deviation of the mean value for each wavelength bin. 

a = 4.05   # log-a spaced wavelength bands. 
           # Present experience indicates that values of a in the range of 
           # 2.5 to 5 are appropriate for most test sites.
           # It is strongly recommended to try several different values to  
           # find the most appropriate a-value for a given dataset. See further
           # in Olafsdottir et al. (2018).
no_std = 1 # Number of standard deviations.

c_TestSite.dc_combination(a)
c_TestSite.plot_combined_dc(plot_all=True)

#%%
# Resample the composite dispersion curve and its upper/lower boundary curves
# at no_points logarithmically or linearly spaced points
no_points = 30
wavelength_min = 'default'
wavelength_max = 'default'
space = 'log' # Logarithmic sampling is recommended 
c_TestSite.resample_dc(space, no_points, wavelength_min, wavelength_max, show_fig=True)

# The composite curve is stored in the dictionary 'resampled' with keys
# 'c_mean', 'c_low', 'c_up' and 'wavelength'
c_mean = c_TestSite.resampled['c_mean']
c_low = c_TestSite.resampled['c_low']
c_up = c_TestSite.resampled['c_up']
wavelengths = c_TestSite.resampled['wavelength']