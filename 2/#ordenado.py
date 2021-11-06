#BURBUJA


def imput():

        c = []

        a = 0

        
        while a != '+':

                c.append(a)

                a = (input('Introduzca los números que desee ordenar:\t'))

        d = c[1:len(c)]

        return d

        #print(d)


def ordenar(d):
        for i in range(0,len(d)-1):
                lista_temp = []
                if d[i+1] > d[i]:
                        temp = d[i+1]
                        d[i+1] == d[i]
                        d[i] == temp
                        print("Valor cambiado")
        print (d)
        return d
                        
                
d = imput()

print(ordenar(d))
