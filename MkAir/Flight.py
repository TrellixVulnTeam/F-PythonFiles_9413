from ContainingClass import SelfContainingClass
from Airport import Airport

class Flight():

    def a(airport: str):
        airP = str(airport).upper()
        return SelfContainingClass.getAirports().get(airP)

    def __init__(self, code, dAirport, aAirport, time, kind, plane, pilot, gate, basePrice, duration):
        self.setCode(code)
        self.setDAirport(dAirport)
        self.setAAirport(aAirport)
        self.setPlane(plane)
        self.setPilot(pilot)
        self.setTime(time)
        self.setKind(kind)
        self.setGate(gate)
        self.setBasePrice(basePrice)
        self.setDuration(duration)
        SelfContainingClass.putFlights(str(self.getDAirport().getAbbreviation()+""+self.getAAirport().getAbbreviation()), self)

        self.hours = self.getDuration()//60
        self.minutes = self.getDuration()-self.hours*60

    def setCode(self, code):
        self.__code = code

    def setDAirport(self, dAirport):
        self.__dAirport = dAirport

    def setAAirport(self, aAirport):
        self.__aAirport = aAirport

    def setTime(self, time):
        self.__time = time

    def setKind(self, kind):
        self.__kind = kind

    def setPlane(self, plane):
        self.__plane = plane

    def setPilot(self, pilot):
        self.__pilot = pilot

    def setGate(self, gate):
        self.__gate = gate

    def getPilot(self):
        return self.__pilot

    def getCode(self):
        return self.__code

    def getDAirport(self):
        return self.__dAirport

    def getAAirport(self):
        return self.__aAirport

    def getTime(self):
        return self.__time

    def getKind(self):
        return self.__kind

    def getPlane(self):
        return self.__plane

    def getGate(self):
        return self.__gate

    def setBasePrice(self, basePrice):
        self.__price = basePrice

    def setDuration(self, duration):
        self.__duration = duration

    def getBasePrice(self):
        return self.__price

    def getDuration(self):
        return self.__duration

    def __str__(self):
        return 'MkAir {} flight {}, from {} ({}) to {} ({}), at {}:{}\nThe base price is {}€ and the duration of the flight will be {}h, {}min\n({}, {} {}, Gate:{}).\n'.format(self.getKind(),
                                                                                                    self.getCode(),
                                                                                                    self.getDAirport().getName(),
                                                                                                    self.getDAirport().getAbbreviation(),
                                                                                                    self.getAAirport().getName(),
                                                                                                    self.getAAirport().getAbbreviation(),
                                                                                                    self.getTime().hour,
                                                                                                    self.getTime().minute,
                                                                                                    self.getBasePrice(),
                                                                                                    str(self.hours),
                                                                                                    str(self.minutes),
                                                                                                    self.getPlane().getName(),
                                                                                                    self.getPilot().getRank(),
                                                                                                    self.getPilot().getSurname(),
                                                                                                    self.getGate())

