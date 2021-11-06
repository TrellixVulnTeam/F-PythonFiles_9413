#Game
import random
logo_1 = '''
1111
  11
  11
  11
111111
'''
logo_2 ='''
 2222
22  22
   22
  22
222222
'''


class Personaje:
        def __init__(self, nombre = '', vida = 100 , ataque = '', defensa = '', logo = ''):
                self.nombre = nombre
                self.vida = vida
                self.ataque = ataque
                self.defensa = defensa
                self.logo = logo

        def __str__ (self):
                return '{} \n La vida de {} es {}\n '.format(self.logo, self.nombre, self.vida)



        def estaMuerto(self):
                if self.vida <= 0:
                        return True
                else:
                        return False

        def atacar(self):
                resultado = self.ataque*random.randrange(100)
                return resultado

        def recibir(self,ataque):
                golpe = self.defensa * ataque
                #inversa = 100 - golpe
                self.vida -= golpe


class Partida:
        def __init__(self, nombre1 = '', nombre2 = '', tiempo = 0):
                self.date = tiempo
                self.P1 = Personaje ( nombre1 , 10000, 0.5, 100, logo_1)
                self.P2 = Personaje ( nombre2 , 10000, 0.5, 100, logo_2)
                self.counter = 1
                self.running = False



        def pegarse(self):
                if self.counter % 2 == 0:
                    self.P2.recibir(self.P1.atacar())
                else:
                    
                    self.P1.recibir(self.P2.atacar())



        def showvidas(self):
                print('{}: {} V.S. {}: {}'.format(self.P1.nombre, self.P1.vida ,self.P2.nombre, self.P2.vida ))



        def terminar(self):
                self.running = False



        def empezar(self):
                self.running = True
                print(self.P1, self.P2)
                while self.running != False:
                        print('\tTurno {}'.format(self.counter))
                        print(self.showvidas())
                        self.pegarse()
                        self.showvidas()
                        if self.P1.estaMuerto() == True or self.P2.estaMuerto() == True :
                                self.terminar()
                        else:
                                self.counter += 1


key = 'p'
while key != 'z':

        nombre1 = input('Nombre del primer jugador\t')
        nombre2 = input('Nombre del segundo jugador\t')

        partida1 = Partida(nombre1, nombre2)

        partida1.empezar()

        key = input("Presione 'z' para salir...")
