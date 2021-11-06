#print( n asteriscos )
def asteriscos(a):
	print(a * '*')
	return None

def estrellas(desde, hasta):
        estrellas = desde * '*'
        for i in range (desde - 1, hasta):
                estrellas = estrellas + '**'
                print(estrellas)
        return None

def triangulo(a):
        estrellas(1,a)

def espacios(desde, hasta):
        espacios = desde * ' '
        for i in range (desde - 1, hasta,-1):
                espacios = espacios + ' ' + estrellas
                print(espacios)
        return None

#ef equilatero(b)



#b = input(('Cuantos quieres imprimir?\t'))
#b = int(b)
asteriscos(5)
estrellas(2,5)
triangulo(10000)
      
