from Planta import Planta
from DeusPark import DeusPark
from Vehiculo import Vehiculo

#Poblamos la planta 1
p1 = Planta(1)

v1 = Vehiculo("BMT216A", "ASTON MARTIN", "DB5", "James Bond", 400, 10.7)
v2 = Vehiculo("JJZ109", "FORD", "MUSTAN", "Bullit", 180, 9.3)
v3 = Vehiculo("OUTATIME", "DELOREAN", "DMC-12", "Emmet Brown", 300, 19.5)
v4 = Vehiculo("KINGHT", "PONTICA", "FIREBIRD", "Michael Knight", 250, 8.4)
v5 = Vehiculo("OUTATIME", "DELOREAN", "DMC-12", "Peter Griffin", 154, 13.2)


p1.agregarVehiculo(v1)
p1.agregarVehiculo(v2)

# Poblamos la planta 2
p2 = Planta(2)
p2.agregarVehiculo(v3)

# Poblamos la planta 3
p3 = Planta(3)
p3.agregarVehiculo(v4)
p3.agregarVehiculo(v5)

aPlantas = []
aPlantas.append(p1)
aPlantas.append(p2)
aPlantas.append(p3)

dp = DeusPark()
dp.poblarParking(aPlantas)

print(dp)
print("Numero de vehiculos: {}".format(dp.getNumeroVehiculos(aPlantas)))
print("Mostrar ocupación: {}".format(dp.mostrarPorcentajeOcupacion(aPlantas)))
print("Buscar mas potente: {}".format(dp.buscarMasPotente(aPlantas)))
print("Consumo medio: {}".format(dp.consumoMedioPorPlanta(aPlantas[0])))
print("Consumo medio por marca (Delorean): {}".format(dp.consumoMedioMarca(aPlantas, "DELOREAN")))

