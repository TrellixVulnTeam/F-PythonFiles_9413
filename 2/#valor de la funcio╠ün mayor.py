#valor de la función mayor

d = []

print('\nPrimera lista\n')

x = True

while x == True:
        
        a = (int)(input('Número: \t'))
        
        d.append(a)
        
        x = (input('¿Quieres seguir introduciendo valores?: \t'))
        
        if x == '-':
                x == False
        else:
                x == True



h = []

print('\nSegunda lista\n')

z = True

while z == True:

        e = (int)(input('Número: \t'))

        h.append(e)

        z = (input('¿Quieres seguir introduciendo valores?: \t'))

        if z == '-':
                z == False
        else:
                z == True
        



if len(d) == len(h):

        contador = 0

        def mayor(d,h):
                for i in range(1, len(h)):
                        if d[i] > h[i]:
                                contadror = contador + 1
                        
                        if contador == len(d):
                                return True
                        else:
                                return False

        print(mayor(d,h))

        print(d)
        print(h)
        
else:
        print('\nLas listas tienen una longitud diferente')
