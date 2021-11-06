#tablas de multiplicar

a = input('¿Cual es la tabla de multiplicar que quieres sacar?\n\t\t')
a = int (a)
for i in range(1,11):
   print(str(a) + ' X ' + str(i) + ' = ' + str(a*i), end = ' ')
      

for i in range(1,11):
      for h in range(1,11):
         print(str(h) + ' X ' + str(i) + ' = ' + str(h*i), ' ') 
