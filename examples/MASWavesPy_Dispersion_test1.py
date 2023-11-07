# -*- coding: utf-8 -*-
"""
Test MASWavesPy Redord and MASWavesPy Dispersion (1)

This example covers the following:
- Import multi-channel seismic data from text files or waveform files 
  (one file for each record). Note that when working with large datasets 
  containing multiple shot gathers, the use of Dataset objects is recommended
  (see Example/MASWavesPy_Dispersion_test2).
- Plot imported data.
- Compute and view the dispersion image (phase velocity spectrum) of the 
  imported data.
- Identify/pick dispersion curve based on spectral maxima (GUI application).
- Return identified dispersion curve as a dictionary.


The following packages are required:
- numpy
- cmath
- matplotlib
- obspy
- tkinter
- copy

Please note that before start using MASWavesPy, it may be neccessary to compile 
the provided pyx files (i.e., compile the cython code used to conduct the 
dispersion processing). See further: http://docs.cython.org/en/stable/src/quickstart/build.html
Please also note that both the provided pyx files must be compiled. 

A setuptools setup.py is provided with the MASWavesPy package. It is recommended
to use it to build the cython code. Note that running setup.py requires the following 
packages:
- distutils
- Cython

How to run setup.py:
1) Open the terminal
2) Navigate to the folder MASWavesPy_master
3) Execute the following command: python maswavespy/setup.py build_ext --inplace

"""
from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")
from maswavespy import wavefield

# ------ Dispersion processing: Import seismic data ------
# Import data from a text file, general requirements:      
# - By default, it is assumed that the recorded data is stored in 
#   a whitespace/tab-delimited text file. If a different string is 
#   used to separate values, it should be provided as an additional 
#   keyword argument (e.g., delimiter=',' for a comma-separated textfile).
# - The number of header lines, including comments, is header_lines.
# - Each trace must be stored in a single column.
# - All traces must be of equal length and missing values are not 
#   allowed (each row in the text file must include the same number
#   of values).
#
# Seismic data can also be imported from any waveform file that can be read by 
# the obspy.read() function from the ObsPy library using the from_waveform
# class method. See https://docs.obspy.org/packages/autogen/obspy.core.stream.read.html
# for a list of supported file formats. 

# Initialize a multi-channel record object from a text file.
file_name = 'Data/Oysand_dx_2m_x1_30m_forward.dat'; header_lines = 5
# Measurement profile set-up
n = 24                 # Number of receivers
direction = 'forward'; # Direction of measurement
dx = 2                 # Receiver spacing [m]
x1 = 30                # Source offset [m]
fs = 1000              # Sampling frequency [Hz]
f_pick_min = 4.5       # Only identify the dispersion curve at frequencies higher or equal to f_pick_min

# Create a multi-channel record object
site = 'Oysand'
profile = 'P1'
rec_TestSite = wavefield.RecordMC.import_from_textfile(site, profile, file_name, header_lines, n, direction, dx, x1, fs, f_pick_min)

# Plot the recorded wavefield
rec_TestSite.plot_data(du=0.75, normalized=False, filled=True)

#%%
# Compute and view dispersion image of recorded wavefield
# Create a elementary dispersion curve object
cT_min = 80; cT_max = 220; cT_step = 0.5
edc_TestSite = rec_TestSite.element_dc(cT_min, cT_max, cT_step)

f_min = 0; f_max = 70
edc_TestSite.plot_dispersion_image(f_min, f_max)

#%%
# Identify elementary dispersion curves (DC) based on spectral maxima.
# The identified DC is saved to the ElementDC object (edc_TestSite in this tutorial).
# Please note that the GUI for dispersion curve identification will open in a new window.
# Instructions on how to use the dispersion curve identification tool are provided.
# within the GUI 
edc_TestSite.pick_dc(f_min, f_max)

#%%
# Return the identified elementary DC as a dictionary. 
edc_TestSite_dict = edc_TestSite.return_to_dict() 

# Plot returned DC
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1,1)
ax.plot(edc_TestSite_dict['f0'], edc_TestSite_dict['c0'],'o'), ax.grid()
ax.set_xlabel('Frequency [Hz]'), ax.set_ylabel('Phase velocity [m/s]')
