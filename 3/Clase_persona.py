#clase_circulo
class persona:
        def __init__(self, altura = 0, edad = 0, peso = 0, sexo = '') :

                self.__altura = altura
                self.__edad = edad
                self.__peso = peso
                self.__sexo = sexo

                
        def __str__ (self):
                return 'la persona tiene {}cm de altura, tiene {} años, pesa {}kg y es {}'.format(self.__altura, self.__edad, self.__peso, self.__sexo)
        
        def getAltura(self):
                return self.__altura
        def getEdad(self):
                return self.__edad 
        def getPeso(self):
                return self.__peso 
        def getSexo(self):
                return self.__sexo 
      

persona1 = persona(123,9, 37, 'Hombre')
persona2 = persona(178,19,45, 'Mujer')


print(persona2)
print(persona1)