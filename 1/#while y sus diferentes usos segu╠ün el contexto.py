#while y sus diferentes usos según el contexto

#a=[[nombre],[apellido_1],[apellido_2]]
a=[[],[],[]]
mas = '+'
while mas == '+':
      respuesta = ''
      print('\nCuando acabe la lista pulse "-" para continuar\n')
      while ( respuesta != '-'):
            nombre = input("Introduce el nombre:\t")
            apellido_1 = input('\nIntroduce el primer apellido:\t')
            apellido_2 = input('\nIntroduce el segundo apellido:\t')
            respuesta = input('\n¿Quiere añadir mas alumnos?\t')
            
            a[0].append(nombre)
            a[1].append(apellido_1)
            a[2].append(apellido_2)
            #a=[[nombre],[apellido_1],[apellido_2]]

      print('En caso de querer imprimir los nombres y apellidos pulse 1:\t')
      print('En caso de querer imprimir los nombres pulse 2:\t')
      print('En caso de querer imprimir los apellidos pulse 3:\t')
      print('En caso de querer imprimir el primer apellido pulse 4:\t')
      selección = input(str('Introduzca su número: \t'))

      if int(selección) == 1:
            print ( a[0] + a[1] + a[2] )
      elif int(selección) == 2:
            print ( a[0] )
      elif int(selección) == 3:
            print ( a[1] + a[2] )
      elif int(selección) == 4:
            print ( a[1] )

      mas = input('¿Quieres añadir algun nombre mas?:\t')
          
#diferencia con "for"
#se utiliza cuando sabemos concretamente el numero de huecos de la lista
#i= variable
#for i in range(0,100)
