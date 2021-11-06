#REPASO ejercicio de lista de piezas de colores

n = ['b','y','y','b','b','y','b','y','y','b']

a = ''

b = ''

c = 'b'
#hacer un programa que haga los soguientes cálculos

contador = 0

counter_b = 0

counter_r = 0

count = 0
print('\nMostrar por pantalla el numero de piezas de la lista\n')

print(len(n))

print('\nContar el número de piezas amarillas\n')
for i in range(len(n)):
   if n[i] == 'y':
      contador = contador + 1
print(int(contador))

print('\nComprobar si no hay piezas amarillas ni azules\n')
for i in range(len(n)):
   if not (n[i] == 'y' or n[i] == 'b'):
      count = count + 1
if count == 0:
   print('No hay piezas de colores diferentes')

print('\nReemplazae todas las piezas amarillas por rojas\n')

for i in range(0,len(n)):
   if n[i] == 'b':
      n[i] = 'r'
print(n)

print('\nSi la ficha azul son 3 puntos y la roja 5 puntos, calcular la puntuación total de la lista\n')

for i in range(len(n)):
   if n[i] == 'b':
      counter_b = counter_b + 1
   elif n[i] == 'r':
      counter_r = counter_r + 1
print(int(counter_b)*3 + int(counter_r)*5)

   
