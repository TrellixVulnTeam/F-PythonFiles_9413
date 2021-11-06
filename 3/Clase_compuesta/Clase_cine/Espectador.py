class Espectador():

    def __init__(self, nombre, edad, dinero):
        self.__nombre = nombre
        self.__edad = edad
        self.__dinero = dinero

    def getDinero(self):
        return self.__dinero

    def getEdad(self):
        return self.__edad

    def getNombre(self):
        return self.__nombre