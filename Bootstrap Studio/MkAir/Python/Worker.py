from Person import Person
from ContainingClass import SelfContainingClass

class Worker(Person):

    def __init__(self, name, surname, workPlace):
        Person.__init__(self, name, surname)
        self.setWorkPlace(workPlace)
        SelfContainingClass.putWorkers(str(self.getName() + "" + self.getSurname()), self)

    def setWorkPlace(self, workPlace):
        self.__workPlace = workPlace

    def getWorkPlace(self):
        return self.__workPlace

    def __str__(self):
        return '{} {} is a {} at MkAir.'.format(self.getName(), self.getSurname(), self.getWorkPlace())
