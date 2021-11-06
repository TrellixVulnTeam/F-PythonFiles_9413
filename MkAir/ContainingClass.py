import pickle


class ContainingClass():
    def __init__(self):
        self.__Workers = {}
        self.__Passengers = {}
        self.__Pilots = {}

        self.__Flights = {}
        self.__Tickets = {}

        self.__Planes = {}
        self.__Airports = {}

        self.__Graph = None
        self.__mGraph = None
        self.__tGraph = None
        self.__wGraph = None
        self.__hGraph = None
        self.__fGraph = None
        self.__sGraph = None
        self.__uGraph = None

    def getGraph(self):
        return self.__Graph

    def putGraph(self, obj):
        self.__Graph = obj

    def getmGraph(self):
        return self.__mGraph

    def putmGraph(self, obj):
        self.__mGraph = obj

    def gettGraph(self):
        return self.__tGraph

    def puttGraph(self, obj):
        self.__tGraph = obj

    def getwGraph(self):
        return self.__wGraph

    def putwGraph(self, obj):
        self.__wGraph = obj

    def gethGraph(self):
        return self.__hGraph

    def puthGraph(self, obj):
        self.__hGraph = obj

    def getfGraph(self):
        return self.__fGraph

    def putfGraph(self, obj):
        self.__fGraph = obj

    def getsGraph(self):
        return self.__sGraph

    def putsGraph(self, obj):
        self.__sGraph = obj

    def getuGraph(self):
        return self.__uGraph

    def putuGraph(self, obj):
        self.__uGraph = obj

    def getWorkers(self):
        return self.__Workers

    def putWorkers(self, key, obj):
        self.__Workers[key] = obj

    def getPassengers(self):
        return self.__Passengers

    def putPassengers(self, key, obj):
        self.__Passengers[key] = obj

    def getPilots(self):
        return self.__Pilots

    def putPilots(self, key, obj):
        self.__Pilots[key] = obj

    def getFlights(self):
        return self.__Flights

    def putFlights(self, key, obj):
        self.__Flights[key] = obj

    def getTickets(self):
        return self.__Tickets

    def putTickets(self, key, obj):
        self.__Tickets[key] = obj

    def getPlanes(self):
        return self.__Planes

    def putPlanes(self, key, obj):
        self.__Planes[key] = obj

    def getAirports(self):
        return self.__Airports

    def putAirports(self, key, obj):
        self.__Airports[key] = obj

    def read(self, fileName):

        binaryFile = open(fileName, "rb")

        data = pickle.load(binaryFile)

        self.__Workers = data[0]
        self.__Passengers = data[1]
        self.__Pilots = data[2]

        self.__Flights = data[3]
        self.__Tickets = data[4]

        self.__Planes = data[5]
        self.__Airports = data[6]

        self.__Graph = data[7]
        self.__mGraph = data[8]
        self.__tGraph = data[9]
        self.__wGraph = data[10]
        self.__hGraph = data[11]
        self.__fGraph = data[12]
        self.__sGraph = data[13]
        self.__uGraph = data[14]

        binaryFile.close()

        print("When file exists")
        for i in data:
            print(i)

    def write(self, fileName):
        data = []
        data.append(self.getWorkers())
        data.append(self.getPassengers())
        data.append(self.getPilots())

        data.append(self.getFlights())
        data.append(self.getTickets())

        data.append(self.getPlanes())
        data.append(self.getAirports())

        data.append(self.getGraph())
        data.append(self.getmGraph())
        data.append(self.gettGraph())
        data.append(self.getwGraph())
        data.append(self.gethGraph())
        data.append(self.getfGraph())
        data.append(self.getsGraph())
        data.append(self.getuGraph())

        binaryFile = open(fileName, "wb")

        pickle.dump(data, binaryFile)

        binaryFile.close()
        del binaryFile

        print("When file is being saved")
        for i in data:
            print(i)


SelfContainingClass = ContainingClass()
