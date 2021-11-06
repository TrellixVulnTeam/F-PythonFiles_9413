#elección de datos de un array introducido y impresión según su introducción
a = ['a','b','c','d','e','f','g','h']
b = ['i','j','k','l','m','n','ñ','o','p','q']
c = ['r','s','t','u','w','x','y','z']
e = ''
while e != '-':
    d = []
    d = str(input('¿Como te llamas?\t'))
    if d[0] in a:
        print ( d + ', tendrás un futuro próspero')            
    elif d[0] in b:
        print ( d + ', algo bueno te ocurrira en las próximas 24h')                 
    elif d[0] in c:
        print ( d + ', podrás conseguir lo que te propongas en tu futuro')    

    e = input('quieres comprobar otro nombre? En caso contrario pulse "-"\t')
                                

            
 
            
        

