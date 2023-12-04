# -*- coding: utf-8 -*-
"""
Test MASWavesPy dataset, wavefield and dispersion modules (2)

This example covers the use of Dataset objects to:
- Initialize a Dataset object.
- Batch import multi-channel seismic data (shot gathers) from a .csv file.
- Remove a record from an initiated Dataset object.
- Add a record to an initiated Dataset object.
- Process each shot gather stored within in the Dataset object and identify
  the corresponding elementary dispersion curve.
- Return the set of identified dispersion curves as a dictionary.
- Initiate a CombineDC object.
- Pickle the dataset object (save the dataset to disk).
    
"""
from maswavespy import dataset

# ------ Dispersion processing: Batch import seismic data from a .csv file ------
# Import from text files, import_format set as 'textfile'
# Import from waveform files, import format set as 'waveform'. 
#
# Required .csv file headings are: 
# 'record_id'    : Unique record identificators (record IDs). 
# 'file_name'    : Path of file with recorded seismic data. For general requirements on
#                  file format, please refer to Example/MASWavesPy_Dispersion_test1
#                  or the documentation of record.py. 
# 'n'            : Number of receivers 
# 'direction'    : Direction of measurement, forward or reverse
# 'dx'           : Receiver spacing [m]
# 'x1'           : Source offset [m]
# In addition, if import_format is 'textfiles'
# 'header_lines' : Number of header lines, including comments
#
# For information on the required datatypes for each of the columns, please 
# refer to the documentation of dataset.py.   

# Initialize a Dataset object
site = 'Oysand'     # Test location
profile = 'P1'      # Profile indentification
date = '00-00-0000' # Date of measurement
fs = 1000           # Sampling frequency [Hz]
f_pick_min = 4.5    # Only identify the dispersion curve at frequencies higher or equal to f_pick_min
TestSite = dataset.Dataset(site, profile, date, fs, f_pick_min)

# Batch import multi-channel seismic data (shot gathers) from a .csv file.
import_format = 'textfile' 
csv_file = 'Data/Oysand_example_dataset.csv' # Path of .csv file
TestSite.records_from_csv(import_format, csv_file)       
print('IDs of records in the database:')
print(TestSite.records.keys()) # IDs of records in the database 

#%%
# Remove a record from an initiated Dataset object.
record_id_to_delete = 'r4'
TestSite.delete_record(record_id_to_delete)
print('IDs of records in the database:')
print(TestSite.records.keys())

#%%
# Add a record to an initiated Dataset object.
record_id_to_add = 'r4'
file_name = 'Data/Oysand_dx_2m_x1_30m_forward.dat'; header_lines = 5
n = 24                # Number of receivers
direction = 'forward' # Direction of measurement
dx = 2                # Receiver spacing [m]
x1 = 30               # Source offset [m]
fs = 1000             # Sampling frequency [Hz]
TestSite.add_from_textfile(record_id_to_add, file_name, header_lines, n, direction, dx, x1)
print('IDs of records in the database:')
print(TestSite.records.keys())

#%%
# Plot the imported multi-channel time series
record_ids_to_plot = ['r1', 'r2', 'r3', 'r4']

for current_id in record_ids_to_plot:
    TestSite.records[current_id].plot_data(translated=True, normalized=False, du=0.75)

#%%
# Process each shot gather stored within in the Dataset object and identify
# the corresponding elementary dispersion curve.
record_ids_to_analyse = ['r1', 'r2', 'r3', 'r4']
f_min = 0; f_max = 70
cT_min = 100; cT_max = 250; cT_step = 0.5

for current_id in record_ids_to_analyse:
    # Initialize an elementary dispersion curve (ElementDC) object.
    TestSite.element_dcs[current_id] = TestSite.records[current_id].element_dc(cT_min, cT_max, cT_step)
    # Pick dispersion curves (GUI opens in a separate window)
    TestSite.element_dcs[current_id].pick_dc(f_min, f_max)

#%%
# Plot and compare picked DCs
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1,1)
for current_id in record_ids_to_analyse:
    ax.plot(TestSite.element_dcs[current_id].f0, TestSite.element_dcs[current_id].c0,'o',label=current_id)
ax.set_xlabel('Frequency [Hz]'), ax.set_ylabel('Phase velocity [m/s]'), ax.grid(); ax.legend()

#%%
# Return the set of identified dispersion curves as a dictionary and
# initiate a CombineDCs object for the dataset.
record_ids = 'all'   # Return all identified dispersion curves.
                     # Alternatively, record_ids can be set as a list of record IDs,
                     # e.g. ['r1', 'r2', 'r3'] if 'r4' should be omitted.
to_CombineDCs = True # Initialize a CombineDCs object for the dataset.

# The CombineDCs object is accessed as Oysand.dcs
TestSite.get_dcs(record_ids, to_CombineDCs)
print(type(TestSite.dcs))

#%%
# Pickle the dataset object.
saveas_filename = 'Oysand_example_dataset'
TestSite.save_to_pickle(saveas_filename)
