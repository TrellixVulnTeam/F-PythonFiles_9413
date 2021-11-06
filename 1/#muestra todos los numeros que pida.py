#muestra todos los numeros que pida

#mostrar los números del 1 al 10
#mostrar los números del 1 al 1000
#mostrar los numeros de 10 en 10 del 20 al 500
#mostrar los números del 10 al 0
while True:
	print('Si quieres mostrar los números del 1 al 10 pulsa 1')
	print('Si quieres mostrar los números del 1 al 1000 pulsa 2')
	print('Si quieres mostrar los números dde 10 en 10 del 20 al 500 pulsa 3')
	print('Si quieres mostrar los números del 10 al 0 pulsa 4')
	a = input('\t')
	if a == '1' :
	   for i in range(1,11):
	      print (i, end = ' ')
	elif a == '2':
	   for i in range(1,1001):
	      print (i, end = ' ')
	elif a == '3':
	   for i in range(20,510, 10):
	      print (i, end = ' ') #cambia el \n que tiene por defecto por un espacio o lo
	elif a == '4':               #declarado entre comillas
	   for i in range(10,-1,-1):
	      print (i, end = ' ')
	else:
	   exit
