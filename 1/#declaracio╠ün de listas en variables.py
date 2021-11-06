#declaración de listas en variables
array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm' ,'n' ,'ñ' ,'o' ,'p' ,'q' ,'r' ,'s' ,'t' ,'u' ,'w' ,'x' ,'y' ,'z' ];
arr = [0,1,2,3,4,5,6,7,8,9]
#arrays dame la lista completa
print (array)
#imprimir lista en un rango
print (array[3:15])
#imprimir los pares del rango 'rango:rango:pares'
print (array[1:9:2])
#dar la vuelta al array
print (array[::-1])
#ultima letra del abecedario
print (array[-1])
#tamaño de el array se suma uno porque no tenemos en cuenta la primera casilla, 'a', porque su valor numérico es '0'
print (len(array)+1)
#saca el numero mas pequeño
print (min(arr))
#saca el numero mas pequeño // 'a' es el valor mas pequeño por el hecho de ser la letra mas pequeña codificada en el código Ascii
print (min(array))
#comprueba si el numero 6 está en la lista 'arr'
print (6 in arr)
#comprueba que el numero 17 no está en la lista 'array'
print ('17' in array)
