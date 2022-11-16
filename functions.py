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
def data_debugger(file_name):
    


if __name__ == "__main__":
	data = np.array([OX, OY_1, OY_2])

	header = ["Miejsce1", "Miejsce2"]

	print(plotmaker(data, header))
