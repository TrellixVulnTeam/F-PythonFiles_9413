#diamond

#5
#    *
#   ***
#  *****
# *******
#*********
# *******
#  *****
#   ***
#    *
#

def imprimirEspacios(numero):
    print(numero * ' ', end = '')

def imprimirAsteriscos(numero):
    print(numero * '*', end = '')


def imprimirRombo(nFilas):
    nRows = int(nFilas*2-1)

    # Inicializar contadores
    nEsp = int(nRows/2)
    nAst = 1
    row = 1
    while(row <= nRows):
        # Imprimir línea
        imprimirEspacios(nEsp)
        imprimirAsteriscos(nAst)
        print()

        # Actualizar contadores
        if(row <= int(nRows/2)):
            nEsp -= 1
            nAst += 2
        else:
            nEsp += 1
            nAst -= 2
        row += 1


nFilas = (int)(input('¿Cuantas filas desea imprimir?:\t'))
imprimirRombo(nFilas)
