
from Heritage.Vehicle import Vehicle


class Motorbike(Vehicle):

    def __init__(self, brand, model, displacement):
        Vehicle.__init__(self,brand,model)
        self.setDisplacement(displacement)

    def setDisplacement(self, displacement):
        self.__displazament = displacement

    def getDisplacement(self):
        return self.__displazament

    def __str__(self):
        return ("Bike brand: " + str(self.getBrand()) + "\nBike model: " + str(
            self.getModel()) + "\nBike gas: " + str(self.getGas()) + "\nBike break: "
                + str(self.getBreak()) + "\nDisplacement: " + str(self.getDisplacement()))



