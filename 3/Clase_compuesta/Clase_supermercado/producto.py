class producto:
	def __init__(self, nombre = '', precio = 0.0, seccion = '', peso = 0.0):
		self.__nombre = nombre
		self.__precio = precio
		self.__seccion = seccion 
		self.__peso = peso

	def __str__(self):
		return f'{self.__nombre}, (precio: {self.__precio}, seccion: {self.__seccion},peso: {self.__peso})'


	def getNombre(self):
		return self.__nombre
	def getPrecio(self):
		return self.__precio
	def getSeccion(self):
		return self.__seccion
	def getPeso(self):
		return self.__peso

	def setNombre(self, nuevo):
		self.__nombre = nuevo
	def setPrecio(self, nuevo):
		self.__preciol = nuevo
	def setSeccion(self, nuevo):
		self.__seccion = nuevo
	def setPeso(self, nuevo):
		self.__peso = nuevo
#en vez de nuevo, poner la primera letra de cada palabra
#	def setNombre(self, n):
#		self.__nombre = n
#	def setPrecio(self, p):
#		self.__preciol = p
#	def setSeccion(self, s):
#		self.__seccion = s
#	def setPeso(self, p):
#		self.__peso = p


	def editar(self):
		self.__nombre = input('introduce el nombre de el producto: ')
		self.__precio = float(input('introduce el precio de el producto: '))
		self.__seccion = input('introduce la seccion de el producto: ')
		self.__peso = float(input('introduce el peso de el producto: '))
