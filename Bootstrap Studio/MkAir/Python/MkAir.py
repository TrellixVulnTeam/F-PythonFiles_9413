import string
from os import path
from random import choice, randint

from AirportMap import airportMap
from ContainingClass import SelfContainingClass
from Flight import Flight
from Pilot import Pilot
from Plane import Plane
from Worker import Worker
from datetime import time
from Passenger import Passenger
from Airport import Airport
import AirportMap


def fourNumbers():
    return str(randint(1000, 9999))


def rdmPilot():
    pilot = choice(list(SelfContainingClass.getPilots()))
    return SelfContainingClass.getPilots().get(pilot)


def rdmGate():
    return str(choice(string.ascii_uppercase)) + str(randint(10, 99))


def rdmPlane():
    while True:
        key = choice(list(SelfContainingClass.getPlanes()))
        if key != "Falcom 7x": break
    return SelfContainingClass.getPlanes().get(key)


saveFile = "data"

if path.exists(saveFile):
    AirportMap.airportMap()
    SelfContainingClass.read(saveFile)


else:

    print("\n#WORKERS")
    mentxaka = Worker("Oier", "Mentxaka", "administrator")
    print(mentxaka)

    print("\n#PASSENGERS")
    aArche = Passenger("Ale", "Arche", 19, "alearche@gmail.com", ["handbag", "Backpack", "Luggage"])
    print(aArche)
    aAGbueno = Passenger("Aida", "Gomezbueno", 19, "agomezbueno@gmail.com", ["handbag", "Backpack", "Luggage"])
    print(aAGbueno)
    mOnaindia = Passenger("Mikel", "Onaindia", 19, "monaindia@gmail.com", ["handbag", "Backpack", "Luggage"])
    print(mOnaindia)
    jDpuebla = Passenger("JonAnder", "DeLaPuebla", 19, "jdpuebla@gmail.com", ["handbag", "Backpack"])
    print(jDpuebla)
    dArias = Passenger("Danel", "Arias", 19, "darias@gmail.com", ["handbag", "Luggage"])
    print(dArias)

    print("\n#PILOTS")
    iDios = Pilot("Iñigo", "DeDios", "Captain")
    print(iDios)
    iYanez = Pilot("IKer", "Yañez", "Captain")
    print(iYanez)
    jBarroeta = Pilot("Jonathan", "Barroeta", "Captain")
    print(jBarroeta)
    oGomila = Pilot("Olatz", "Gomila", "Captain")
    print(oGomila)
    mIbarra = Pilot("Marta", "Ibarra", "Captain")
    print(mIbarra)

    print("\n#AIRPORTS")
    bio = Airport("Loiu", "BIO", [True, True, True, False, False, False, True])
    print(bio)
    mad = Airport("Madrid Barajas", "MAD", [False, True, False, True, False, False, True])
    print(mad)
    yyz = Airport("Vancouver", "YYZ", [False, False, True, True, False, True, True])
    print(yyz)
    nyc = Airport("New York", "NYC", [True, True, False, False, True, False, True])
    print(nyc)
    lax = Airport("Los Angeles", "LAX", [True, False, True, True, True, False, False])
    print(lax)
    mex = Airport("Ciudad de México", "MEX", [True, True, True, False, False, False, False])
    print(mex)
    lgw = Airport("London Gatwik", "LGW", [True, False, True, False, True, False, True])
    print(lgw)
    cdg = Airport("Paris Charles de Gaulle", "CDG", [True, False, True, False, True, False, True])
    print(cdg)
    svo = Airport("Moscú Sheremétievo", "SVO", [False, True, False, True, True, False, True])
    print(svo)
    cpt = Airport("Ciudad del Cabo", "CPT", [True, False, True, True, False, False, False])
    print(cpt)
    hnd = Airport("Tokyo Haneda", "HND", [False, False, False, True, True, True, False])
    print(hnd)
    syd = Airport("Sydney Kingsford Smith", "SYD", [False, True, True, True, False, False, False])
    print(syd)

    print("\n#PLANES")
    B747 = Plane("Boeing 747", 50)
    print(B747)
    B727 = Plane("Boeing 727", 15)
    print(B727)
    A320 = Plane("Airbus A320", 22)
    print(A320)
    A318 = Plane("Airbus A318", 12)
    print(A318)
    f7x = Plane("Falcom 7x", 6)
    print(f7x)

    print("\n#FLIGHTS")
    print("#DEPARTURES")

    # TODO TODAS LAS HORAS HAY QUE CONTROLARLAS

    print(
        Flight("MK" + fourNumbers(), bio, lgw, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 386, 110))
    print(
        Flight("MK" + fourNumbers(), bio, cdg, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 118, 100))
    print(
        Flight("MK" + fourNumbers(), bio, mad, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 276, 65))
    print(
        Flight("MK" + fourNumbers(), mad, svo, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 552, 505))
    print(
        Flight("MK" + fourNumbers(), lax, mad, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 1253,
               780))

    print(
        Flight("MK" + fourNumbers(), mad, nyc, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 860, 480))
    print(
        Flight("MK" + fourNumbers(), mad, mex, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 735, 665))
    print(
        Flight("MK" + fourNumbers(), mex, hnd, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 1283,
               1040))
    print(
        Flight("MK" + fourNumbers(), mex, lax, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 319, 255))
    print(
        Flight("MK" + fourNumbers(), lax, nyc, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 256, 350))

    print(
        Flight("MK" + fourNumbers(), lax, cpt, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 2066,
               1680))
    print(
        Flight("MK" + fourNumbers(), cpt, lgw, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 840,
               1285))
    print(
        Flight("MK" + fourNumbers(), lgw, cdg, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 246, 75))
    print(
        Flight("MK" + fourNumbers(), lgw, nyc, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 1424,
               475))
    print(
        Flight("MK" + fourNumbers(), cdg, syd, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 1551,
               1270))

    print(
        Flight("MK" + fourNumbers(), cdg, hnd, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 1577,
               715))
    print(
        Flight("MK" + fourNumbers(), hnd, svo, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 4576,
               825))
    print(
        Flight("MK" + fourNumbers(), svo, yyz, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 3645,
               840))
    print(
        Flight("MK" + fourNumbers(), yyz, syd, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 1185,
               1560))
    print(
        Flight("MK" + fourNumbers(), yyz, mad, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 2185,
               815))

    print("#ARRIVALS")

    print(
        Flight("MK" + fourNumbers(), lgw, bio, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 386, 110))
    print(
        Flight("MK" + fourNumbers(), cdg, bio, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 118, 100))
    print(
        Flight("MK" + fourNumbers(), mad, bio, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 276, 65))
    print(
        Flight("MK" + fourNumbers(), svo, mad, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 552, 505))
    print(
        Flight("MK" + fourNumbers(), mad, lax, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 1253,
               780))

    print(
        Flight("MK" + fourNumbers(), nyc, mad, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 860, 480))
    print(
        Flight("MK" + fourNumbers(), mex, mad, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 735, 665))
    print(
        Flight("MK" + fourNumbers(), hnd, mex, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 1283,
               1040))
    print(
        Flight("MK" + fourNumbers(), lax, mex, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 319, 255))
    print(
        Flight("MK" + fourNumbers(), nyc, lax, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 256, 350))

    print(
        Flight("MK" + fourNumbers(), cpt, lax, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 2066,
               1680))
    print(
        Flight("MK" + fourNumbers(), lgw, cpt, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 840,
               1285))
    print(
        Flight("MK" + fourNumbers(), cdg, lgw, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 246, 75))
    print(
        Flight("MK" + fourNumbers(), nyc, lgw, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 1424,
               475))
    print(
        Flight("MK" + fourNumbers(), syd, cdg, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 1551,
               1270))

    print(
        Flight("MK" + fourNumbers(), hnd, cdg, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 1577,
               715))
    print(
        Flight("MK" + fourNumbers(), svo, hnd, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 4576,
               825))
    print(
        Flight("MK" + fourNumbers(), yyz, svo, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 3645,
               840))
    print(
        Flight("MK" + fourNumbers(), svo, yyz, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 1185,
               1560))
    print(
        Flight("MK" + fourNumbers(), mad, yyz, time(10, 30), "Commercial", rdmPlane(), rdmPilot(), rdmGate(), 2185,
               815))

    AirportMap.airportMap()

    SelfContainingClass.write(saveFile)

AirportMap.allPaths(0, AirportMap.a("bio"), AirportMap.a("lax"), "All week")
# AirportMap.allPaths(0, AirportMap.a("hnd"), AirportMap.a("bio"), "All week")
# AirportMap.allPaths(0, AirportMap.a("mad"), AirportMap.a("cpt"), "All week")

AirportMap.allPaths(1, AirportMap.a("bio"), AirportMap.a("lax"), "Monday")
AirportMap.allPaths(2, AirportMap.a("nyc"), AirportMap.a("BIO"), "Tuesday")
AirportMap.allPaths(3, AirportMap.a("syd"), AirportMap.a("yyz"), "Wednesday")
AirportMap.allPaths(4, AirportMap.a("mad"), AirportMap.a("svo"), "Thursday")
AirportMap.allPaths(5, AirportMap.a("hnd"), AirportMap.a("cpt"), "Friday")
AirportMap.allPaths(6, AirportMap.a("bio"), AirportMap.a("lax"), "Saturday")
AirportMap.allPaths(7, AirportMap.a("lgw"), AirportMap.a("yyz"), "Sunday")
