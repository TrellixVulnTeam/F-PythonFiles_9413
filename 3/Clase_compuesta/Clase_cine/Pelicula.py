class Pelicula():

    def __init__(self, titulo, duracion, edad_minima, director):
        self.__titulo = titulo
        self.__duracion = duracion
        self.__edad_minima = edad_minima
        self.__director = director

    def getTitulo(self):
        return self.__titulo

    def getEdadMinima(self):
        return self.__edad_minima