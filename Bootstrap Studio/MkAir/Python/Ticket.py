from Passenger import Passenger
from Flight import Flight

class Ticket():
    def __init__(self, passenger, flight):
        self.setFlight(flight)
        self.setPassenger(passenger)

    def setPassenger(self,passenger):
        self.__passenger = passenger

    def setFlight(self,flight):
        self.__flight = flight

    def getPassenger(self):
        return self.__passenger

    def getFlight(self):
        return self.__flight

    def __str__(self):
        return ""