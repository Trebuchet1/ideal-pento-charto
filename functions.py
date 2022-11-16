import numpy as np
from matplotlib import pyplot as plt
import math
import os
import glob



# Grzegorz
def datachange(lista):
    print("Specify how you want to change your data, for a variable use 'x' If you would rather not do that just put down 'NO'.  Example: x*100-70")
    F = input()
    if F=="NO":
        print("Skipped")
    else:
        l=len(lista)
        dane = [0]*l


        i=0
        while i<l-1 :
            x = lista[i]
            dane[i]=eval(F)
            i+=1
        print(dane)
        return(dane)

def datachange_mass(lista, funkcja):
        l=len(lista)
        dane = [0]*l
        i=0
        while i<l-1 :
            x = lista[i]
            dane[i]=eval(funkcja)
            i+=1
        print(dane)
        return(dane)


# Jasiek


# Piotr
def plotmaker(data, header):

	fig, ax = plt.subplots()

	for i in range(1, len(header)):
		ax.plot(data[:, 0], data[:, i], label = header[i])

	plt.xlabel("C stężenie")
	plt.ylabel("Y sygnał")
	plt.legend()
	plt.show()

# NOTE: this one just checks if a file even has data
def file_debugger(file):
    source = open(file)
    decimals = [',', '/s']
    skippy = 0
    for i in range(20):
        line = source.readline()
        try:
            for i in decimals:
                [float(n.strip()) for n in line.split(i)]
        except ValueError:
            skippy +=1
        else:
            return [skippy, i]
    print('looks like {} is corrupted, look for hints in readme'.format(file))
    return None

def array_creator(files_list):
    # NOTE: check if the file even has data in the first 20 lines
    # TODO: make the 20 lines adjustable in config
    header = ['x_label']
    data = [[]]
    for file in files_list:
        f_row, decimal = file_debugger(file)
        if f_row == None:
            continue

        t_data = file.readlines()[f_row-1]
        t_header = t_data.pop(0).split(decimal)
        header[0] = t_header[0]
        header.append(t_header[1:])
        
        t_data = [[float(n.strip()) for n in i.split(decimal)] for i in t_data]
        t_data = np.array(t_data).transpose().tolist()
        data[0] = t_data[0]
        data.append(data[1:])
    return header, np.array(data)

if __name__ == "__main__":
    print('you ran the wrong file, run main.py!')
