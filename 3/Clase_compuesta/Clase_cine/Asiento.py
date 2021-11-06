class Asiento():

    def __init__(self, fila, col):
        self.__fila = fila
        self.__columna = col
        self.__ocupado = False

    def getColumna(self):
        return self.__columna

    def getFila(self):
        return self.__fila

    def isOcupado(self):
        return self.__ocupado

    def setOcupado(self, oc):
        self.__ocupado = oc

    def __str__(self):
        estado = ""
        if (self.isOcupado()):
            estado = "Ocup."
        else:
            estado = "Libre"
        return "{} {} : {}".format(self.__fila, self.__columna, estado)
