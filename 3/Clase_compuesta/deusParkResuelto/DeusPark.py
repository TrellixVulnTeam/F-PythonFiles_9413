class DeusPark():

    def __init__(self):
        self.__plantas = []

    def poblarParking(self, aPlantas):
        self.__plantas = aPlantas
    
    def getNumeroVehiculos(self, aPlantas):
        cont = 0
        for i in range(len(aPlantas)):
            cont += aPlantas[i].getNumeroVehiculos()
        return cont
    
    def mostrarPorcentajeOcupacion(self, aPlantas):
        plazasDisponibles = 0
        plazasOcupadas = 0
        for i in range(len(aPlantas)):
            plazasDisponibles += aPlantas[i].getPlazasPlanta()
            plazasOcupadas += aPlantas[i].getNumeroVehiculos()
        
        return plazasOcupadas / plazasDisponibles

    def buscarMasPotente(self, aPlantas):
        vehiculo = None
        potencia = 0
        for i in range(len(aPlantas)):
            aVehiculos = aPlantas[i].getVehiculos()
            for j in range(len(aVehiculos)):
                if aVehiculos[j].getCV() > potencia:
                    potencia = aVehiculos[i].getCV()
                    vehiculo = aVehiculos[i]
        return vehiculo
    
    def consumoMedioPorPlanta(self, aPlantas):
        consumoAcumulado = self.calcularConsumoMedioVechiculos(aPlantas.getVehiculos())
        return consumoAcumulado

    def calcularConsumoMedioVechiculos(self, aVehiculos):
        consumoAcumulado = 0
        for i in range(len(aVehiculos)):
            consumoAcumulado += aVehiculos[i].getConsumo()
        return consumoAcumulado / len(aVehiculos)

    def consumoMedioMarca(self, aPlantas, marca):
        aVehiculosMarca = []

        #Primero obtenemos todos los coches de la marca que hay
        for i in range(len(aPlantas)):
            aVehiculosPlanta = aPlantas[i].getVehiculos()
            for j in range(len(aVehiculosPlanta)):
                if aVehiculosPlanta[j].getMarca() == marca:
                    aVehiculosMarca.append(aVehiculosPlanta[j])
        
        # Calculamos el consumo medio
        return self.calcularConsumoMedioVechiculos(aVehiculosMarca)

    def __str__(self):
        cadena = ""
        for i in range(len(self.__plantas)):
            cadena += str(self.__plantas[i]) + "\n"
        return cadena



