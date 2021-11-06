
class Vehicle():
    def __init__(self, brand, model):
        self.setBrand(brand)
        self.setModel(model)
        self.__gas = False
        self.__break = False

    def setBrand(self,brand):
        self.__brand = brand

    def setModel(self,model):
        self.__model = model

    def setGas(self,boolean):
        self.__gas = boolean

    def setBreak(self,boolean):
        self.__break = boolean

    def getBrand(self):
        return self.__brand

    def getModel(self):
        return self.__model

    def getGas(self):
        return self.__gas

    def getBreak(self):
        return self.__break

    def __str__(self):
        return ("Vehicle brand: " + str(self.getBrand()) + "\nVehicle model: " + str(self.getModel()) + "\nVehicle gas: " + str(self.getGas()) + "\nVehicle break: "+ str(self.getBreak()))

