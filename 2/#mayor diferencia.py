#mayor diferencia

c = []

b = 0

while b != '+' :
        b = int(b)
        
        c.append(b)
        
        b = (input('Introduzca un número\t'))

a = c[1:]

def mayorDiferencia(a):
   
   númeroMayor = a[0]

   númeroMenor = a[0]

   for i in range(1, len(a)):
      if a[i] > númeroMayor:
         númeroMayor = a[i]
      elif a[i] < númeroMenor:
         númeroMenor = a[i]
   respuesta = númeroMayor - númeroMenor
   return ( respuesta )

print (mayorDiferencia(a))
