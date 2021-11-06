#clase_fecha

class fecha:

    def __init__(self, dia = 0 , mes = 0 , anyo = 0):

        self.__dia = dia
        self.__mes = mes
        self.__anyo = anyo

        def getDia(self):
            return self.__dia
        def getMes(self):
            return self.__mes
        def getAnyo(self):
            return self.__anyo
        def setDia(self):
            return self.__dia = dia
        def setMes(self):
            return self.__mes = mes
        def setAnyo(self):
            return self.__anyo = anyo

        def __str__(self):
            return '{}, {}, {}'.format(self.getDia(), self.getMes(), self.getAnyo())

        def nombreMes(self):
            if self.getMes()() == 1:
                return Enero
            if getMes() == 2:
                return Febrero
            if getMes() == 3:
                return Marzo
            if getMes() == 4:
                return Abril
            if getMes() == 5:
                return Mayo
            if getMes() == 6:           #darme el nombre del mes
                return Junio
            if getMes() == 7:
                return Julio
            if getMes() == 8:
                return Agosto
            if getMes() == 9:
                return Septiembre
            if getMes() == 10:
                return Octubre
            if getMes() == 11:
                return Noviembre
            if getMes() == 12:
                return Diciembre

        def diaSiguiente(self):
            if self.getMes() > 12:
                print ('ERROR')
            elif self.getMes() < 1 :
                print ('ERROR')         #acotacion parametrica
            elif self.getDia() > 31:
                print ('ERROR')
            elif self.getDia() < 1:
                print ('ERROR')
            else:
                if self.getMes() == 12:
                    if self.getDia() == 31:
                        self.getDia(dia) = 1
                        self.getMes(mes) = 1         #diciembre
                        self.getAnyo(anyo) += 1
                    else:
                        self.getDia(dia) += 1
                elif self.getMes() == 2:
                    if self.getAnyo() % 4 == 0:
                        if self.getDia() == 28:
                            self.getDia(dia) += 1     #febrero con sus bisiestos
                        elif self.getDia() == 29:
                            self.getDia(dia) = 1
                            self.getMes(mes) += 1
                    elif self.getAnyo()  % 4 != 0 and self.getDia() == 28:
                        self.getDia(dia) = 1
                        self.getMes(mes) += 1
                    elif self.getAnyo() % 4 == 0 or self.getAnyo() % 4 != 0 and self.getDia() != 28 and self.getDia() != 29:
                        self.getDia(dia) += 1

                elif self.getMes() != 4 or self.getMes() != 6 or self.getMes() != 9 or self.getMes() != 10 :
                    if self.getDia() == 31:
                        self.getDia(dia) = 1
                        self.getMes(mes) += 1
                    else:
                        self.getDia(dia) += 1

                else:
                    if self.getDia() == 30:
                        self.getDia(dia) = 1
                        self.getMes(mes) += 1
                    else:
                        self.getDia(dia) += 1


fecha1 = fecha(11,11,2011)
print(fecha1)
print(fecha1.nombreMes())
print(fecha1.diaSiguiente())
