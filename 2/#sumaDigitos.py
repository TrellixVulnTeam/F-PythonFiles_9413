#SumaDígitos

a = input('introduzca una frase que contenga números:\t')

def sumaDigitos(a):
        cont = 0

        for i in range(0,len(a)):
                if a[i] == '1':
                        cont += 1
                elif a[i] == '2':
                        cont += 2
                elif a[i] == '3':
                        cont += 3
                elif a[i] == '4':
                        cont += 4
                elif a[i] == '5':
                        cont += 5
                elif a[i] == '6':
                        cont += 6
                elif a[i] == '7':
                        cont += 7
                elif a[i] == '8':
                        cont += 8
                elif a[i] == '9':
                        cont += 9
                elif a[i] == '0':
                        cont += 0
        return print (cont)

sumaDigitos(a)
