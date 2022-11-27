import numpy as np
from matplotlib import pyplot as plt
import re


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
    dec = ['.', ',', '.', '.']
    whs = ['\s', '\s', ';', ',']
    skippy = 0
    for i in range(4):
        line = source.readline()
        for i in range(3):
            try:
                t_line = [x.replace(dec[i], '.') for x in re.split(whs[i], line) if x]
                [float(n) for n in t_line]
            except:
                continue
            else:
                return [skippy, dec[i], whs[i]]
        skippy+=1
    print('looks like {} is corrupted, look for hints in readme'.format(file))
    return None

def array_creator(files_list):
    # NOTE: check if the file even has data in the first 20 lines
    # TODO: make the 20 lines adjustable in config
    header = ['x_label']
    data = [[]]
    for file in files_list:
        decision = file_debugger(file)
        if decision == None:
            continue
        f_row, dec, whs = decision
        f = open(file)
        t_data = f.readlines()[(f_row-1):]
        t_header = [x for x in re.split(whs,t_data.pop(0)) if x]
        header[0] = t_header[0]
        header += t_header[1:]
        
        t_data = [[float(x.replace(dec, '.')) for x in re.split(whs, line) if x] for line in t_data]
        t_data = np.array(t_data).transpose().tolist()
        data[0] = t_data[0]
        data += t_data[1:]
    if len(header) != len(data):
        print('looks like you have different syntax in headers and data\nI am generating my own')
        header = [header[0]] + ['series '+str(i) for i in range(len(data)-1)]
    header = [i.replace('\n','') for i in header]
    return header, data

if __name__ == "__main__":
    print('you ran the wrong file, run main.py!')
