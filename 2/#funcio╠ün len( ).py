#función len( )

a = [1,2,3,4,5,6,7,8,9]

def tamaño(lista):
      contador = 0
      for i in range(0,len(lista)):
            contador = contador + 1
      return contador

print( tamaño(a))
