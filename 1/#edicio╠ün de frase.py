#edición de una frase
a = []

c = ''

a = input('Introduzca una frase:\t ')

temp = ''

while c != 'no':
#contar espacios
        print('Si quieres contar el número de espacios de el texto pulse 1')
        print('Si quieres sustituir las vocales de la frase por asteriscos pulse 2')
        print('Si quieres darle la vuelta al texto pulse 3')
        b = input('¿Que quieres hacer?\t')
        contador = 0
        if b == '1':
                for i in range(0,len(a)):                               
                        if a[i] == ' ':
                               contador = contador + 1
                print (contador)
        elif b == '2':
        #sustituir las vocales por asteríscos
                for i in range(0,len(a)):
                        if a[i] == 'a':
                                temp = temp + '*'
                        elif a[i]  == 'e':
                                temp = temp + '*'
                        elif a[i] == 'i':
                                temp = temp + '*'
                        elif a[i] == 'o':
                                temp = temp + '*'
                        elif a[i] == 'u':
                                temp = temp + '*'
                        else:
                                temp = temp + a[i]
                a = temp
                print (a)
                
        elif b == '3':
        #darle vuelta al array
                print (a[::-1])
                       
        c = input('¿Quiere continuar trabajando con esta frase?\t')
print('Ahora trabajemos con numeros, imprimiremos los números enteros del 1 al 100')

d = -1
while d < 100:
        d = d + 1
        print (d, end = ' ')

print('Ahora sustituiremos los múltiplos de 3 por "Fizz"')
e = -1

while e < 100:
        
        e = e + 1
        
        if (e % 3 == 0 and e % 5 == 0):
                print('fizzbuzz', end = ' ')
        elif (e % 3) == 0:
                print('fizz', end = ' ')
        elif ( e % 5) == 0:
                print('buzz', end = ' ')
        else:
                print(e, end = ' ')
        #print (e, end = ' ')
        


#elif e % 5 == '0':
 #               e == 'Buzz'
  #      elif  e % 3 and e % 5 == '0':
   #             e == 'FizzBuzz'            



















