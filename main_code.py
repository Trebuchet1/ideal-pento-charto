import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import os
import glob

config = open('config.txt', 'r').read()
# NOTE: creates a list of files within a folder specified in config file
folder = config.split('\n')[2].split('=')[1].strip() 
from_col = int(config.split('\n')[5].split('=')[1])
to_col = int(config.split('\n')[6].split('=')[1])

# NOTE: gets the current directory
cwd = os.getcwd() 
# NOTE: creates a list of files in a directory we want
files = sorted(glob.glob(os.path.join(cwd, folder,"*.txt"))) 
print('Used files:\n', ',\n'.join([os.path.basename(x) for x in files]))

header = []
for x in range(0, len(files)):
    t_file = open(files[x], 'r')
    print('loaded')
    t_header = t_file.readline().split()
    t_array = np.loadtxt(t_file, skiprows=1)
    data = t_array[0,:]
    for x in range(from_col, to_col):
        header.append(t_header[x])
        np.append(data, t_array[x, :])
# NOTE: header is a list of column names
# NOTE: data is a numpy array of data coresponding to header
