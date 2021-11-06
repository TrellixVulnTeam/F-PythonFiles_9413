class Vehiculo:
    
    def __init__(self, Matricula = '', Marca ='', Modelo = '', Usuario = '', CV = 0, Consumo = 0 ):

        self.__matricula = Matricula
        self.__marca = Marca
        self.__modelo = Modelo
        self.__usuario = Usuario
        self.__cv = 0
        self.__consumo = 0
        self.setCV(CV)
        self.setConsumo(Consumo)

    def getMatricula(self):
        return self.__matricula
    def getModelo(self):
        return self.__modelo
    def getMarca(self):
        return self.__marca
    def getUsuario(self):
        return self.__usuario
    def getCV(self):
        return self.__cv
    def getConsumo(self):
        return self.__consumo

    def setConsumo(self, consumo):
        if consumo > 0:
            self.__consumo = consumo

    def setCV(self, cv):
        if cv > 0 and cv <= 400:
            self.__cv = cv

    def __str__(self):
        return 'El vehiculo con matrícula {} conducido por {} es un {} {} de {} caballos y su consumo es de {} '.format(self.getMatricula(), self.getUsuario(), self.getMarca(), self.getModelo(), self.getCV(), self.getConsumo())
