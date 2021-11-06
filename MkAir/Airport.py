from ContainingClass import SelfContainingClass

class Airport():

    def assignToGraph(self):
        if self.getDays()[0]:
            SelfContainingClass.putmGraph(self)
        if self.getDays()[1]:
            SelfContainingClass.puttGraph(self)
        if self.getDays()[2]:
            SelfContainingClass.putwGraph(self)
        if self.getDays()[3]:
            SelfContainingClass.puthGraph(self)
        if self.getDays()[4]:
            SelfContainingClass.putfGraph(self)
        if self.getDays()[5]:
            SelfContainingClass.putsGraph(self)
        if self.getDays()[6]:
            SelfContainingClass.putuGraph(self)

    def __init__(self, name, abbreviation,days):
        self.setName(name)
        self.setAbbreviation(abbreviation)
        self.setDays(days)
        SelfContainingClass.putAirports(self.getAbbreviation(), self)
        self.assignToGraph(self)

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAbbreviation(self, abb):
        self.__abb = abb

    def getAbbreviation(self):
        return self.__abb

    def setDays(self, days):
        self.__days = days

    def getDays(self):
        return self.__days

    def getDaysString(self):
        str = ""
        if self.getDays()[0]:
            str += "MON "
        if self.getDays()[1]:
            str += "TUE "
        if self.getDays()[2]:
            str += "WED "
        if self.getDays()[3]:
            str += "THU "
        if self.getDays()[4]:
            str += "FRI "
        if self.getDays()[5]:
            str += "SAT "
        if self.getDays()[6]:
            str += "SUN "

        return str

    def __str__(self):
        return 'MkAir operates at {} airport ({}) on {}.'.format(self.getName(), self.getAbbreviation(),self.getDaysString())

