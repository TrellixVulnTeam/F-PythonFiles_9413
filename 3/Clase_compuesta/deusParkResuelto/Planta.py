class Planta():

    def __init__(self, id, plazasPlanta = 100):
        self.__id = id
        self.__plazasPlanta = plazasPlanta
        self.__vehiculos = []

    def getId(self):
        return self.__id

    def getPlazasPlanta(self):
        return self.__plazasPlanta

    def getNumeroVehiculos(self):
        return len(self.__vehiculos)

    def getPlazasLibresPlanta(self):
        return self.__plazasPlanta - self.getNumeroVehiculos()

    def getPorcentajaOcupacion(self):
        return self.getNumeroVehiculos()/self.__plazasPlanta

    def getVehiculos(self):
        return self.__vehiculos

    def agregarVehiculo(self, vehiculo):
        self.__vehiculos.append(vehiculo)

    def __str__(self):
        return "Planta {} ({} vechiculos, {} plazas disponibles)".format(self.__id, self.getNumeroVehiculos(), self.getPlazasLibresPlanta())
