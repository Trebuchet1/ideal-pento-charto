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

# Datagrabber - it finds the array and delimiter and header in the file
# even if there is lots of unwanted crap placed there by the user
def file_dubugger(file_name):
    file = open(file_name, 'r')
    skip = 0
    delimiters = [', ', ' ']
    line = []
    for x in range(1, 40):
        header = line
        line = file.readline()
        for dl in delimiters:
            try:
                missing_line = [[float(x.strip()) for x in line.split(dl)]]
            except ValueError:
                skip += 0.5
            else:
                t_array = np.loadtxt(file, delimiter = dl)
                t_array = np.concatenate((missing_line, t_array))
                skip = math.ceil(skip)
                header_search = open(file_name)
                t_list = []
                for x in range(skip):
                    t_list.append(header_search.readline().strip())
                t_header = list(filter(None, t_list))[-1].split(dl)
                return t_array, t_header


if __name__ == "__main__":
	data = np.array([OX, OY_1, OY_2])

	header = ["Miejsce1", "Miejsce2"]

	print(plotmaker(data, header))
