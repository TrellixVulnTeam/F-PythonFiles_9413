from Cine import Cine
from Pelicula import Pelicula
from Espectador import Espectador
import random
if __name__ == "__main__":
    columnas = "ABCDEFGHI"
    p = Pelicula("El rey Leon", 200, 10, "Jon Favreu")
    c = Cine(20, p)

    e1 = Espectador("B. Wayne", 20, 200000000)
    e2 = Espectador("D. Grayson", 2, 200)

    c.sentarEspectador(e1, 2, "A")
    c.sentarEspectador(e2, 1, "B")

    for i in range(20):
        nombre = "Espectador_" + str(i)
        edad = random.randrange(90)
        dinero = random.randrange(200000)

        e = Espectador(nombre,edad,dinero)
        fila = random.randrange(9)
        columna = columnas[random.randrange(len(columnas))]
        c.sentarEspectador(e, fila, columna)

    c.imprimirSala()

