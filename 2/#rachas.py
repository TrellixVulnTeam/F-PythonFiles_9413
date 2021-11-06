#rachas

def rachas(lista):
        eR = False
        contador = 0
        for i in range(0,len(lista) - 1):
                if lista[i] == lista[i + 1]:
                        eR = True
                if (eR and lista[i] != lista[ i+1 ]):
                        eR = False
                        contador += 1
        if eR == True:
                        contador += 1
        return contador
        
print(rachas([1,2,3,4,4,5,6]))
print(rachas([1,1,1,4,4,6,6]))
