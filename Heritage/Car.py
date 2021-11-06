
from Heritage.Vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, brand, model, doorNum):
        Vehicle.__init__(self,brand,model)
        self.setDoorNum(doorNum)

    def setDoorNum(self, num):
        self.__doorNum = num

    def getDoorNum(self):
        return self.__doorNum

    def __str__(self):
        return ("Car brand: " + str(self.getBrand()) + "\nCar model: " + str(
            self.getModel()) + "\nCar gas: " + str(self.getGas()) + "\nCar break: "
                + str(self.getBreak()) + "\nNumber of doors: " + str(self.getDoorNum()))


