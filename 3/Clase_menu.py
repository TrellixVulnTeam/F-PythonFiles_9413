#clase_circulo
class menu:
        def __init__(self,entrantes = '', primero = '', segundo = '', postre = '', bebida = '', pan = '') :

                self.__entrantes = entrantes
                self.__primero = primero
                self.__segundo = segundo
                self.__postre = postre
                self.__bebida = bebida
                self.__pan = pan

                
        def __str__ (self):
                return 'el menú consta de un entrante  de {} un primer plato de {} un segundo plato de {} un postre de {} bebida {} y {}'.format(self.__entrantes, self.__primero, self.__segundo, self.__postre ,self.__bebida,self.__pan)
        
        def getEntrantes(self):
                return self.__entrantes
        def getPrimero(self):
                return self.__primero 
        def getSegundo(self):
                return self.__segundo 
        def getPostre(self):
                return self.__postre 
        def getBebida(self):
                return self.__bebida 
        def getPan(self):
                return self.__pan       º

Menu1 = menu(primero = 'macarrones',segundo = 'lomo',postre = 'yogur',bebida = 'agua')
Menu2 = menu(entrantes = 'foie con escamas de sal ', primero = 'crema de finas verduras', segundo = 'ternera asada al toque de arandano', postre = 'cama de hojaldre desmigada con tarta de trufa', bebida = 'vega sicilia cosecha 2011', pan ='Pan')


print(Menu1)
print(Menu2)