from ContainingClass import SelfContainingClass
from Person import Person


class Passenger(Person):

        def __init__(self, name, surname, age, email, luggage):
                Person.__init__(self,name,surname)
                self.setAge(age)
                self.setEmail(email)
                self.setLuggage(luggage)
                SelfContainingClass.putPassengers(str(self.getEmail()),self)


        def setAge(self, age):
                self.__age = age

        def setLuggage(self, luggage):
                self.__luggage = luggage

        def getAge(self):
                return self.__age

        def getLuggage(self):
                return self.__luggage

        def getEmail(self):
                return self.__email

        def setEmail(self, email):
                self.__email = email

        def __str__ (self):
                return '{} {}, a {} year old passenger, with {} email, has {} luggage packages.'.format(self.getName(), self.getSurname(), self.__age,self.getEmail(), len(self.getLuggage()))



