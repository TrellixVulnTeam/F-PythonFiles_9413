#rima

pal1 = input('introduzca la primera palabra con la que desee trabajar: ')

pal2 = input('introduzca la segunda palabra con la que desee trabajar: ')

n = (int)(input('¿Cuales son las útimas letras que desea comparar?'))

def rima(pal1, pal2, n):
        for i in range(0,len(pal1)):
                a = pal1[:-n]
        for i in range(0, len(pal2)):
                b = pal2[:-n]
                
        if a == b:
                print( 'True' ) 
        else:
                print( 'False' )

print(rima(pal1, pal2, n))
