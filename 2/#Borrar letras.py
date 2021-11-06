#Borrar letras

a = (str)(input('Palabra de la que deseas borrar letras:\t'))
b = (str)(input('\nLetras que deseas eliminar de la palabra:\t'))


def borrarLetras(a,b):
        temp = ''

        for i in range(0,len(a)):
                found=False
                for j in range(0,len(b)):
                        if a[i] == b[j]:
                                found = True
                if(not found):
                        temp += a[i]
        return (temp)


print(borrarLetras(a,b))
                          
