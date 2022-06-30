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
    data = np.array([t_array[0,:]])
    for x in range(from_col, to_col):
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