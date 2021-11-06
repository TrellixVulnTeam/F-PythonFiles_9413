#clase_baraja
import random
class cartas:

    def __init__(self, 1 ,2 , 3 ,4,5,6,7,s,c,r):

    	
    	self.__1 = 1
    	self.__2 = 2
    	self.__3 = 3
    	self.__4 = 4
    	self.__5 = 5
    	self.__6 = 6
    	self.__7 = 7
    	self.__s = s
    	self.__c = c
    	self.__r = r
    def __str__(self):
    	return 'el {}, el {}, el {}, el {}, el {}, el {}, el {}, el {}, el {} y el {}'.format(self.__1,self.__2,self.__3,self.__4,self.__5,self.__6,self.__7,self.__s,self.__c,self.__r)

    def barajar(self):
    	random.randrange(baraja[i])
    def siguienteCarta(self):
    	pass
    def cartasDisponibles(self):
    	pass
    def darCartas(self):
    	pass
    def cartasMonton(self):
    	pass
    def mostrarBaraja

bastos = bastos('1 bastos','2bastos','3bastos','4bastos','5bastos','6bastos','7bastos','sbastos','cbastos','rbastos')
print(bastos)