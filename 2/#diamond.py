#diamond

nFilas = (int)(input('¿Cuantas filas desea imprimir?:\t'))

'''
                
def asteriscos(a):
5
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

'''

nRows = int(nFilas * 2 - 1)
nEsp = int(nRows / 2)
nAst = 1

for i in range(1,nRows):
        #imprimir espacios
        espacios = ' '
        for j in range(1, nEsp):
                espacios += ' '
        #imprimir "*"
        asteriscos = '*'
        for k in range(1, nAst):
                asteriscos += "*"
        print(espacios + asteriscos)
        # Actualizar contadores
        if (i <= int(nRows / 2)):
                nEsp = nEsp - 1
                nAst = nAst + 2
        else:
                nEsp = nEsp + 1
                nAst = nAst - 2

nEsp = nEsp + 1
nAst = nAst -2
espacios += 
print(espacios + asteriscos)
