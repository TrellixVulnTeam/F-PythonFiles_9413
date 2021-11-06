from producto import * 
class Pedido:
	def __init__(self, codigo = 0, cliente = '', productos = []):
		self.__codigo = codigo
		self.__cliente = cliente
		self.__productos = productos

	def __str__(self):
		resultado = f'{self.__codigo}, {self.__cliente}, ['
		for producto in self.__productos:
			resultado = resultado + str(producto)  
		resultado = resultado + ' ] '
		return resultado


	def getCodigo(self):
		return self.__codigo
	def getCliente(self):
		return self.__cliente
	def getProductos(self):
		return self.__productos

	def setCodigo(self, nuevo):
		self.__codigo = nuevo
	def setCliente(self, nuevo):
		self.__cliente = nuevo
	def setProductos(Self, nuevo):
		self.__productos = nuevo

	def getPrecioTotal(self):
		total = 0
		for p in self.__productos:
			total = total + p.getPrecio()
		return total


