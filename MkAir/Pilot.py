from Person import Person
from ContainingClass import SelfContainingClass


class Pilot(Person):

    def __init__(self, name, surname, rank):
        Person.__init__(self, name, surname)
        self.setRank(rank)
        SelfContainingClass.putPilots(self.getName() + "" + self.getSurname(), self)

    def setRank(self, rank):
        self.__rank = rank

    def getRank(self):
        return self.__rank

    def __str__(self):
        return '{} {} is a {} at MkAir.'.format(self.getName(), self.getSurname(), self.getRank())
