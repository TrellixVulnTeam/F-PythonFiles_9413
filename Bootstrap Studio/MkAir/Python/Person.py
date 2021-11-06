class Person():
    def __init__(self, name, surname):
        self.setName(name)
        self.setSurname(surname)

    def __str__(self):
        return 'The registered person is {} {}'.format(self.__name, self.__surname)

    def setSurname(self, surname):
        self.__surname = surname

    def setName(self, name):
        self.__name = name

    def getSurname(self):
        return self.__surname

    def getName(self):
        return self.__name
