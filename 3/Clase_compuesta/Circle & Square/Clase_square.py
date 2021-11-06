#clase_square
import math
class square:
        def __init__(self,sideA = 0, sideB = 0, color = ''):
                self.__sideA = sideA
                self.__sideB = sideB
                self.__color = color
                self.__op = sideA * sideB
                
        def __str__ (self):
                return 'Rectangulo de lado {} y color {}'.format(self.__side, self.__color)
        def getColor(self):
        	return self.__color
        def getSideA(self):
        	return self.__sideA
        
        def getSideB(self):
        	return self.__sideB
        def getArea(self):
        	return self.__op



