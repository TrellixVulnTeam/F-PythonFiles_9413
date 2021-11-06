from ContainingClass import SelfContainingClass

class Plane():

    def __init__(self, name, pasNum):
        self.setName(name)
        self.setPassengerNumber(pasNum)
        SelfContainingClass.putPlanes(self.getName(), self)

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setPassengerNumber(self, pasNum):
        self.__pasNum = pasNum

    def getPassengerNumber(self):
        return self.__pasNum

    def __str__(self):
        return 'MkAir operates with {}s which have {} available places.'.format(self.getName(), self.getPassengerNumber())
