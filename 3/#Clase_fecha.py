#clase_fecha

class Fecha():
        def __init__(self, day = 0, month = 0, year = 0):
                self.day = day
                self.month = month
                self.year = year
                
        def __str__ (self):
                return '{}-{}-{}'.format(self.day, self.month, self.year)


fecha1 = Fecha(3,5,2019)
fecha2 = Fecha(20,2,2020)

print(fecha1)
print(fecha2)
