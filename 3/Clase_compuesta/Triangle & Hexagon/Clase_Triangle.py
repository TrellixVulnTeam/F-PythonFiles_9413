#clase_triangle

class triangle:
    def __init__(self, apotema = 0, side = 0):
        self.__apotema = apotema
        self.__side = side
        self.__op = side * apotema / 2
        
    def getApotema(self):
        return self.__apotema
    def getSide(self):
        return self.__side
    def getOp(self):
        return self.__op
    
    def __str__(self):
        return 'The triangle with side {} and apotema {} has a {}cm^2 area'.format(self.__side, self.__apotema, self.__op)
