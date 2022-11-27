import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc
import os

# NOTE: file imports
from functions import *

font = {'family':'serif'}
rc('font', **font)

# NOTE: gets the current directory
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


folder_name = config[7].split('=')[1].strip()
files_list = [i.strip() for i in config[10].split('=')[1].split(',')]

# NOTE: creates a list of specified files if there is anything in the config
file_names = [i for i in os.listdir('./' + str(folder_name)) if '.csv' in i]
if files_list != ['']:
    file_names = [i for i in file_names if i in files_list]
files = [('./'+folder_name+'/'+i) for i in file_names]
print('Using files:\n', '\n'.join(file_names))

# NOTE: creating the combined array, welcome to hell
# NOTE: resulting header is a list, data is a numpy array
header, data = array_creator(files)
data = np.array(data)


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
        ax.plot(data[0], data[i], label = header[i])
    plt.xlabel(header[0])
    plt.ylabel("intensywność sygnału [j.a.]")
    plt.legend()
    plt.show()
