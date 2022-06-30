
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
