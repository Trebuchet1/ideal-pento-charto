import numpy as np
from matplotlib import pyplot as plt
import math
import os
import glob

# NOTE: file imports
from functions import *

# NOTE: gets the current directory
cwd = os.getcwd()
config = open('config.txt', 'r').read().split('\n')

# NOTE: creates a list of files within a folder specified in config file
type1 = int(config[3].split('=')[1]) # NOTE: types
type2 = int(config[4].split('=')[1])
type3 = int(config[5].split('=')[1])
folder = config[7].split('=')[1].strip() # NOTE: folder

# NOTE: chosen columns
from_col = config[13].split('=')[1]
if from_col == True:
    from_col = int(from_col)
to_col = config[14].split('=')[1]
if to_col == True:
    to_col = int(from_col)
files_list = config[10].split('=')[1]

# NOTE: file names
if files_list.strip():
    # NOTE: creates a list of specified files if there is anything in the config
    files = [os.path.join(os.path.dirname(cwd), folder,x.strip()) for x in files_list.split(',')]
    print('Using files:\n', '\n'.join([os.path.basename(x) for x in files]))
else:
    # NOTE: creates a list of all files in a directory we want
    files = sorted(glob.glob(os.path.join(os.path.dirname(cwd), folder,"*.txt")))
    filenames = [os.path.basename(x) for x in files]
    print('Using files:\n', ',\n'.join(filenames))


# NOTE: creating the combined array, welcome to hell
header = []
for file_name in files:
    print('loaded')
    #refer to functions file for description
    t_array, t_header = file_dubugger(file_name)
    if file_name == files[0]:
        header.append(t_header[0])
        data = np.transpose(np.array([t_array[:, 0]]))
    if not (isinstance(from_col, str) or isinstance(to_col, str)):
            header += t_header[from_col:to_col]
            data = np.concatenate((data, t_array[from_col:to_col, :]), axis = 1)
    else:
        header += [(x + ' ' + os.path.basename(file_name)) for x in t_header[1:]]
        data = np.concatenate((data, t_array[:, 1:]), axis = 1)
print(header)
print(data)
# NOTE: header is a list of column names
# NOTE: data is a numpy array of data coresponding to header


#Grzes robi teraz fragment
if type3 == 1:
    data[:,0]=(datachange(data[:,0]))
    print("Wpisz fukcję dla reszty kolumn Y lub NIE by pominąć")
    funkcja=input()
    if funkcja == "NIE":
        print("Skip")
    else:
        i=0
        while i<len(data[:,0]):
            data[i,:]=datachange_mass(data[i,:],funkcja)
            i=i+1

#Jas pracuje od tego momentu ;)
if type2 == 1:
    fig, ax = plt.subplots()
    #definig fuction for derivatives
    def D(x,y):
        yprime = np.diff(y)/np.diff(x)
        xprime=[]
        for i in range(len(yprime)):
            xtemp = (x[i+1]+x[i])/2
            xprime = np.append(xprime,xtemp)
        return xprime, yprime
    #loops for making data
    axx = data[0, :]
    for x in range(1, (len(header)+1)):
        axy = data[x, :]
        xprime, yprime = D(axx,axy)
        ax.plot(xprime,yprime,label = ("Derivative of " + header[x-1]))
    for x in range(1, (len(header)+1)):
        axy = data[x, :]
        xprime, yprime = D(axx,axy)
        xprime, yprime = D(xprime, yprime)
        ax.plot(xprime,yprime,label = ("2nd derivative of " + header[x-1]))
    #making labels
    plt.xlabel(header[0])
    plt.ylabel(":)")
    plt.legend()
    plt.show()

# Piotr
if type1 == 1:
    fig, ax = plt.subplots()
    for i in range(1, len(header)):
        ax.plot(data[:, 0], data[:, i], label = header[i])
    plt.xlabel(header[0])
    plt.ylabel("Y sygnał")
    plt.legend()
    plt.show()
