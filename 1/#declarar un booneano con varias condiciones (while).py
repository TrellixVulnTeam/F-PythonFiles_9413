#declarar un booleanp con varias condiciones (While)
num = input ( 'Dame un número\t' )
#comparamos los valores de el numero o letra metido en la variable 'num'
#con un 'try:' que comrara los distintos tipos de variables asignadas durante el
#código
try:
    #declaramos la variable 'number' con el numero entero de 'num'
    number = int(num) #si 'num' es un número entero entonces declaramos la 
                      #variable 
    if (number > 50):
        print ('Es un número mayor que 50')
    else :
        print ('Es un número menor que 50')
except ValueError:
    print ('Esto no es un número')
