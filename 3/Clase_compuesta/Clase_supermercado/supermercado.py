from producto import *
from pedido import *

#crear 5 objetos de la clase producto
arroz = producto('arroz', 5.5, 'arroces', 1.1)
queso = producto('queso', 2.2, 'charcuteria', 2.2)
jamon = producto('jamon',  4.4, 'charcuteria', 1.1)
pasta = producto('pasta', 3.3, 'pasta', 8.1)
tomate = producto('tomate', 2.2, 'botes', 2.2)

productos = [arroz, queso, jamon, pasta, tomate]

#crear 3 pedidos con al menos 3 productos cada uno 
pedido1 = pedido(1, 'juan', [queso, jamon, pasta])
pedido2 = pedido(2, 'pedro',[queso, arroz, pasta])
pedido3 = pedido(3, 'carlos', [jamoon, arroz, tomate])

pedidos = [pedido1, pedido2, pedido3]

#menu:

while (opcion != '0'):
	print('1. listar los productos disponibles')
	print('2. listar los pedidos realizados')
	print('3. añadir un producto nuevo')
	print('4. listar los clientes que han hecho un pedido')
	print('0. salir')
	opcion = input('¿opcion?')

	if (opcion == '1'):
		for p in productos:
			print(p)
		#listar los productos disponibles
	elif (opcion == '2'):#listar pedidos realizados
		for p in pedidos:
			print(p)
	elif (opcion == '3'):
		nuevo = producto()
		nuevo.editar()
		productos.append(nuevo)
	elif (opcion == '4'):
		clientes = []
		for p in pedidos:
			cliente = p.getClientes()
			if(cliente not in cliente):
				clientes.append(cliente)
		print(clientes)

