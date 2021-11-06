#clase_circulo
import math
class circle:
        def __init__(self,radius = 0, color = ''):
                self.__radius = radius
                self.__color = color
                self.__op = math.pi * pow(radius, 2)
                
        def __str__ (self):
                return 'Círculo de radio {} y color {}'.format(self.__radius, self.__color)
        def getColor(self):
        	return self.__color
        def getRadius(self):
        	return self.__radius
        def getArea(self):
        	return self.__op




