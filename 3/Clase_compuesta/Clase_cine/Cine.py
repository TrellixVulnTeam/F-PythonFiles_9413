from Asiento import Asiento
from Espectador import Espectador

class Cine():

    def __init__(self, precio, pelicula):
        self.__pelicula = pelicula
        self.__precio = precio

        # Inicializamos los asientos
        self.__asientos = []

        self.__cadena = 'ABCDEFGHI'

        for i in range(8):
            col = []
            for j in range(9):
                a = Asiento(i + 1, self.__cadena[j])
                col.append(a)
            self.__asientos.append(col)

    def getPelicula(self):
        return self.__pelicula

    def sentarEspectador(self, espectador, fila, columna):
        if self.__asientoCorrecto(fila, columna) and espectador.getDinero() > self.__precio \
                and espectador.getEdad() > self.__pelicula.getEdadMinima():
            self.__ocuparAsiento(fila, columna)
            print(espectador.getNombre() + " ha ocupado su asiento.")
        else:
            print("Lo siento {}, no cumple las condiciones para ver la pelicula.".format(espectador.getNombre()))

    def __asientoCorrecto(self, fila, columna):
        if((fila > len(self.__asientos) and fila < 0)  and columna > 'A' and columna < self.__cadena[-1]):
            return False
        else:
            asiento = self.__asientos[fila - 1][self.__getPosicionColumna(columna)]
            return not asiento.isOcupado()

    def __ocuparAsiento(self, fila, columna):
        self.__asientos[fila - 1][self.__getPosicionColumna(columna)].setOcupado(True)

    def __getPosicionColumna(self, letra):
        for i in range(len(self.__cadena)):
            if(letra == self.__cadena[i]):
                return i
        return -1


    def imprimirSala(self):
        for i in range(len(self.__asientos)):
            for j in range(len(self.__asientos[i])):
                print(self.__asientos[i][j], end='\t')
            print("")