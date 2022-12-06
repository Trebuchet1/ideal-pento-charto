import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc
import os

#file imports
from functions import *

#font
font = {'family':'serif'}
rc('font', **font)

#gets the current directory
config = open('config.txt', 'r').read().split('\n')

#type of chart modification
type1 = int(config[3].split('=')[1]) #types
type2 = int(config[4].split('=')[1])
type3 = int(config[5].split('=')[1])

from_col = config[13].split('=')[1] #chosen columns
if from_col == True:
    from_col = int(from_col)
to_col = config[14].split('=')[1]
if to_col == True:
    to_col = int(to_col)

folder_name = config[7].split('=')[1].strip() #foldername
files_list = [i.strip() for i in config[10].split('=')[1].split(',')] #list of files


min_x = config[20].split('=')[1] #range x
if min_x: min_x = float(min_x)
else: min_x=None
max_x = config[21].split('=')[1]
if max_x: 
    max_x = float(max_x)
    print('tes')
else: max_x=None

invert = int(config[24].split('=')[1]) #invert x axis bool

annots = []
if not config[27].split('=')[1]:
    annots = config[27].split('=')[1].strip().split(', ') #annotations instructions
    annots = [i[1:-1].split(',') for i in annots]
    annots = [[float(i[0]), int(i[1])] for i in annots]

y_name = 'data'
if y_name != '': y_name = config[27].split('=')[1].strip()

#creates a list of specified files if there is anything in the config
file_names = [i for i in os.listdir('./' + str(folder_name)) if '.csv' in i]
if not files_list:
    file_names = [i for i in file_names if i in files_list]
files = [('./'+folder_name+'/'+i) for i in file_names]
print('Using files:\n', '\n'.join(file_names))

#creating the combined array
#resulting header is a list, data is a numpy array
header, data = array_creator(files)
data = np.array(data)

#slice the array
from_x, to_x = slicer(data[0], min_x, max_x)
data = np.array([i[from_x:to_x] for i in data])

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

def fannot(ax, x_value,col,data):
    for i in range(len(data[0])):
        if data[0][i]<x_value and data[0][i+1]>x_value:
            ax.annotate(str(round(data[0][i])),(data[0][i],data[col][i])).draggable()
            ax.scatter(data[0][i], data[col][i], c='black', s=5, zorder=2)


# Piotr
if type1 == 1:
    fig, ax = plt.subplots()
    for i in range(1, len(header)):
        ax.plot(data[0], data[i], label = header[i], zorder=1)
    plt.xlabel(header[0])
    plt.xlim(min_x,max_x)
    plt.ylabel(y_name)
    plt.legend()
    plt.tight_layout()
    if invert == 1: ax.invert_xaxis()
    for an in annots:
        fannot(ax, an[0], an[1], data)
    plt.show()

