import numpy as np
from matplotlib import pyplot as plt
import math
import os
import glob


# Datagrabber - it finds the array and delimiter and header in the file
# even if there is lots of unwanted crap placed there by the user
def file_dubugger(file):
    skip = 0
    delimiters = [', ', ' ']
    line = []
    for x in range(1, 40):
        header = line
        line = file.readline()
        for dl in delimiters:
            try:
                missing_line = [float(x.strip()) for x in line.split(dl)]
                missing_line = np.array([[x] for x in missing_line])
            except ValueError:
                skip += 0.5
            else:
                t_array = np.loadtxt(file, delimiter = dl)
                t_array = np.insert(t_array, 0, missing_line, axis = 0)
                t_header = [x.strip() for x in header.split(dl)]
                return t_array, t_header


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

	fig = plt.figure(figsize=(14, 4))

	for i in range(1, len(data) ):

		plt.plot( data[0, :], data[i, :], label = header[i -1])

	plt.xlabel("C stężenie")
	plt.ylabel("Y sygnał")

	plt.legend()
	plt.show()

	fig, ax = plt.subplots()

if __name__ == "__main__":
	data = np.array([OX, OY_1, OY_2])

	header = ["Miejsce1", "Miejsce2"]

	print(plotmaker(data, header))
