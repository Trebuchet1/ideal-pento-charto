import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import os
import glob
<<<<<<< HEAD
# NOTE: gets the current directory
cwd = os.getcwd()
=======
>>>>>>> origin/main
config = open('config.txt', 'r').read()
# NOTE: creates a list of files within a folder specified in config file
type1 = int(config.split('\n')[3].split('=')[1]) # NOTE: types
type2 = int(config.split('\n')[4].split('=')[1])
type3 = int(config.split('\n')[5].split('=')[1])
folder = config.split('\n')[7].split('=')[1].strip() # NOTE: folder

from_col = config.split('\n')[13].split('=')[1] # NOTE: chosen columns
if from_col == True:
    from_col = int(from_col)
to_col = config.split('\n')[14].split('=')[1]
if to_col == True:
    to_col = int(from_col)
files_list = config.split('\n')[10].split('=')[1]

if files_list.strip():
    # NOTE: creates a list of specified files if there is anything in the config
    files = [os.path.join(os.path.dirname(cwd), folder,x.strip()) for x in files_list.split(',')]
    print('Using files:\n', '\n'.join([os.path.basename(x) for x in files]))
else:
    # NOTE: creates a list of all files in a directory we want
    files = sorted(glob.glob(os.path.join(os.path.dirname(cwd), folder,"*.txt")))
    print('Using files:\n', ',\n'.join([os.path.basename(x) for x in files]))

header = []
for x in range(0, len(files)):
    t_file = open(files[x], 'r')
    print('loaded')
    t_header = t_file.readline().split()
    t_array = np.loadtxt(t_file, skiprows=1)
    print(t_header)
    if x == 0:
        header.append(t_header[0])
    if not isinstance(from_col, str) or not isinstance(to_col, str):
        for x in range(from_col, to_col):
            header.append(t_header[x])
            data = np.append(data, [t_array[x, :]], axis = 0)
    else:
        for x in range(0, len(t_header)):
            header.append(t_header[x])
            data = np.append(data, [t_array[x, :]], axis = 0)
# NOTE: header is a list of column names
# NOTE: data is a numpy array of data coresponding to header
#Grzes robi teraz fragment
dataX=data
dataX[0,:]=(datachange(data[0,:]))
print("Wpisz fukcję dla reszty kolumn Y lub NIE by pominąć")
funkcja=input()
if funkcja == "NIE":
    print("Skip")
else:
    i=0
    while i<len(data[:,0]):
        dataX[i,:]=datachange_mass(data[i,:],funkcja)
        i=i+1

#Jas pracuje od tego momentu ;)
<<<<<<< HEAD
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
    print(header)
    plt.xlabel(header[0])
    plt.ylabel(":)")
    plt.legend()
    plt.show()
=======
print("Array Dimension = ",len(data.shape))
fig, ax = plt.subplots()

def D(x,y):
    yprime = np.diff(y)/np.diff(x)
    xprime=[]
    for i in range(len(yprime)):
        xtemp = (x[i+1]+x[i])/2
        xprime = np.append(xprime,xtemp)
    return xprime, yprime

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

plt.xlabel(header[0])

plt.ylabel(":)")
plt.legend()
plt.show

#Peter 
>>>>>>> origin/main
