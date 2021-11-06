#clase_Main
import math
from Clase_circulo import circle 
from Clase_square import square 

C1 = circle(9,'Rojo')

print(C1.getColor())
print(C1.getRadius())
print(C1.getArea())

S1 = square(3,2,'Verde')

print(S1.getColor())
print(S1.getSideA())
print(S1.getSideB())
print(S1.getArea())
