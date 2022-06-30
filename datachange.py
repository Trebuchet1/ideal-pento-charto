'''
import //dane które analiujemy
import //funkcja którą rysujemy wykresy as wykres
'''
def datachange(lista):
    print("Podaj jakim zmianą chcesz poddać dane. zmienną nazwij x. Jesli nie chcesz edytowac danych wpisz NIE  Przykład: x*100-70")
    F = input()
    if F=="NIE":
        print("Pominięto")
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
    
datachange()
