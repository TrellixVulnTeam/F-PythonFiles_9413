from os import path
from Airport import Airport
from ContainingClass import SelfContainingClass
import networkx as nx

def a(airport: str):
    airP = str(airport).upper()
    return SelfContainingClass.getAirports().get(airP)

def airportMap():
    saveFile = "data"

    if path.exists(saveFile):
        map = SelfContainingClass.getGraph()
        mon = SelfContainingClass.getmGraph()
        tue = SelfContainingClass.gettGraph()
        wed = SelfContainingClass.getwGraph()
        thu = SelfContainingClass.gethGraph()
        fri = SelfContainingClass.getfGraph()
        sat = SelfContainingClass.getsGraph()
        sun = SelfContainingClass.getuGraph()

    else:
        map = nx.DiGraph()

        # VUELOS DE IDA
        map.add_edge(a("bio"), a("lgw"))
        map[a("bio")][a("lgw")]["price"] = 386
        map[a("bio")][a("lgw")]["duration"] = 110
        map.add_edge(a("bio"), a("cdg"))
        map[a("bio")][a("cdg")]["price"] = 118
        map[a("bio")][a("cdg")]["duration"] = 100
        map.add_edge(a("bio"), a("mad"))
        map[a("bio")][a("mad")]["price"] = 276
        map[a("bio")][a("mad")]["duration"] = 65
        map.add_edge(a("mad"), a("svo"))
        map[a("mad")][a("svo")]["price"] = 552
        map[a("mad")][a("svo")]["duration"] = 505
        map.add_edge(a("mad"), a("nyc"))
        map[a("mad")][a("nyc")]["price"] = 860
        map[a("mad")][a("nyc")]["duration"] = 480
        map.add_edge(a("mad"), a("mex"))
        map[a("mad")][a("mex")]["price"] = 735
        map[a("mad")][a("mex")]["duration"] = 655
        map.add_edge(a("mex"), a("hnd"))
        map[a("mex")][a("hnd")]["price"] = 1283
        map[a("mex")][a("hnd")]["duration"] = 1040
        map.add_edge(a("mex"), a("lax"))
        map[a("mex")][a("lax")]["price"] = 319
        map[a("mex")][a("lax")]["duration"] = 255
        map.add_edge(a("lax"), a("nyc"))
        map[a("lax")][a("nyc")]["price"] = 256
        map[a("lax")][a("nyc")]["duration"] = 350
        map.add_edge(a("lax"), a("cpt"))
        map[a("lax")][a("cpt")]["price"] = 2066
        map[a("lax")][a("cpt")]["duration"] = 1680
        map.add_edge(a("cpt"), a("lgw"))
        map[a("cpt")][a("lgw")]["price"] = 840
        map[a("cpt")][a("lgw")]["duration"] = 1285
        map.add_edge(a("lgw"), a("cdg"))
        map[a("lgw")][a("cdg")]["price"] = 246
        map[a("lgw")][a("cdg")]["duration"] = 75
        map.add_edge(a("lgw"), a("nyc"))
        map[a("lgw")][a("nyc")]["price"] = 1424
        map[a("lgw")][a("nyc")]["duration"] = 475
        map.add_edge(a("cdg"), a("syd"))
        map[a("cdg")][a("syd")]["price"] = 1551
        map[a("cdg")][a("syd")]["duration"] = 1270
        map.add_edge(a("cdg"), a("hnd"))
        map[a("cdg")][a("hnd")]["price"] = 1577
        map[a("cdg")][a("hnd")]["duration"] = 715
        map.add_edge(a("hnd"), a("svo"))
        map[a("hnd")][a("svo")]["price"] = 4576
        map[a("hnd")][a("svo")]["duration"] = 825
        map.add_edge(a("svo"), a("yyz"))
        map[a("svo")][a("yyz")]["price"] = 3645
        map[a("svo")][a("yyz")]["duration"] = 840
        map.add_edge(a("yyz"), a("syd"))
        map[a("yyz")][a("syd")]["price"] = 1185
        map[a("yyz")][a("syd")]["duration"] = 1560
        map.add_edge(a("yyz"), a("mad"))
        map[a("yyz")][a("mad")]["price"] = 2185
        map[a("yyz")][a("mad")]["duration"] = 815
        map.add_edge(a("lax"), a("mad"))
        map[a("lax")][a("mad")]["price"] = 1253
        map[a("lax")][a("mad")]["duration"] = 780

        # VUELOS DE VUELTA
        map.add_edge(a("lgw"), a("bio"))
        map[a("lgw")][a("bio")]["price"] = 340
        map[a("lgw")][a("bio")]["duration"] = 110
        map.add_edge(a("cdg"), a("bio"))
        map[a("cdg")][a("bio")]["price"] = 200
        map[a("cdg")][a("bio")]["duration"] = 100
        map.add_edge(a("mad"), a("bio"))
        map[a("mad")][a("bio")]["price"] = 296
        map[a("mad")][a("bio")]["duration"] = 65
        map.add_edge(a("svo"), a("mad"))
        map[a("svo")][a("mad")]["price"] = 752
        map[a("svo")][a("mad")]["duration"] = 505
        map.add_edge(a("nyc"), a("mad"))
        map[a("nyc")][a("mad")]["price"] = 360
        map[a("nyc")][a("mad")]["duration"] = 480
        map.add_edge(a("mex"), a("mad"))
        map[a("mex")][a("mad")]["price"] = 795
        map[a("mex")][a("mad")]["duration"] = 665
        map.add_edge(a("hnd"), a("mex"))
        map[a("hnd")][a("mex")]["price"] = 1290
        map[a("hnd")][a("mex")]["duration"] = 1040
        map.add_edge(a("lax"), a("mex"))
        map[a("lax")][a("mex")]["price"] = 318
        map[a("lax")][a("mex")]["duration"] = 255
        map.add_edge(a("nyc"), a("lax"))
        map[a("nyc")][a("lax")]["price"] = 512
        map[a("nyc")][a("lax")]["duration"] = 350
        map.add_edge(a("cpt"), a("lax"))
        map[a("cpt")][a("lax")]["price"] = 2600
        map[a("cpt")][a("lax")]["duration"] = 1680
        map.add_edge(a("lgw"), a("cpt"))
        map[a("lgw")][a("cpt")]["price"] = 1040
        map[a("lgw")][a("cpt")]["duration"] = 1285
        map.add_edge(a("cdg"), a("lgw"))
        map[a("cdg")][a("lgw")]["price"] = 300
        map[a("cdg")][a("lgw")]["duration"] = 75
        map.add_edge(a("nyc"), a("lgw"))
        map[a("nyc")][a("lgw")]["price"] = 1244
        map[a("nyc")][a("lgw")]["duration"] = 475
        map.add_edge(a("syd"), a("cdg"))
        map[a("syd")][a("cdg")]["price"] = 1151
        map[a("syd")][a("cdg")]["duration"] = 1270
        map.add_edge(a("hnd"), a("cdg"))
        map[a("hnd")][a("cdg")]["price"] = 1764
        map[a("hnd")][a("cdg")]["duration"] = 715
        map.add_edge(a("svo"), a("hnd"))
        map[a("svo")][a("hnd")]["price"] = 4990
        map[a("svo")][a("hnd")]["duration"] = 825
        map.add_edge(a("yyz"), a("svo"))
        map[a("yyz")][a("svo")]["price"] = 2456
        map[a("yyz")][a("svo")]["duration"] = 840
        map.add_edge(a("syd"), a("yyz"))
        map[a("syd")][a("yyz")]["price"] = 1625
        map[a("syd")][a("yyz")]["duration"] = 1560
        map.add_edge(a("mad"), a("yyz"))
        map[a("mad")][a("yyz")]["price"] = 2625
        map[a("mad")][a("yyz")]["duration"] = 815
        map.add_edge(a("mad"), a("lax"))
        map[a("mad")][a("lax")]["price"] = 1853
        map[a("mad")][a("lax")]["duration"] = 780

        def generateSubgraph(originalGraph, removingNodes: []):
            subG = nx.DiGraph()
            subG.add_nodes_from(originalGraph.nodes)
            subG.add_edges_from(originalGraph.edges)
            for i in removingNodes:
                subG.remove_node(i)
            return subG

        def printDay(day,cal):
            string = day + " "
            for i in cal.nodes:
                string += i.getAbbreviation() + " "
            return print(string)

        mon = generateSubgraph(map,[a("mad"),a("svo"),a("syd"),a("yyz"),a("hnd")])
        printDay("MON",mon)
        tue = generateSubgraph(map,[a("lgw"),a("cdg"),a("cpt"),a("yyz"),a("lax"),a("hnd")])
        printDay("TUE",tue)
        wed = generateSubgraph(map,[a("mad"),a("svo"),a("nyc"),a("hnd")])
        printDay("WED",wed)
        thu = generateSubgraph(map,[a("lgw"),a("cdg"),a("bio"),a("mex"),a("nyc")])
        printDay("THU",thu)
        fri = generateSubgraph(map,[a("bio"),a("mad"),a("cpt"),a("mex"),a("yyz"),a("syd")])
        printDay("FRI",fri)
        sat = generateSubgraph(map,[a("cpt"),a("mex"),a("lax"),a("syd"),a("lgw"),a("cdg"),a("bio"),a("svo")])
        printDay("SAT",sat)
        sun = generateSubgraph(map,[a("mad"),a("hnd"),a("cpt"),a("mex"),a("lax"),a("syd")])
        printDay("SUN",sun)


        sAir = "The availabe airports are "
        try:
            for i in SelfContainingClass.getGraph().nodes:
                sAir += str(i.getName() + " " + i.getAbbreviation() + " ")
            print(sAir)

            sMon = "The availabe airports on monday are "
            for i in SelfContainingClass.getmGraph().nodes:
                sMon += str(i.getName() + " " + i.getAbbreviation() + " ")
            print(sMon)

            sTue = "The availabe airports on tuesday are "
            for i in SelfContainingClass.gettGraph().nodes:
                sTue += str(i.getName() + " " + i.getAbbreviation() + " ")
            print(sTue)

            sWed = "The availabe airports on wednesday are "
            for i in SelfContainingClass.getwGraph().nodes:
                sWed += str(i.getName() + " " + i.getAbbreviation() + " ")
            print(sWed)

            sThu = "The availabe airports on thursday are "
            for i in SelfContainingClass.gethGraph().nodes:
                sThu += str(i.getName() + " " + i.getAbbreviation() + " ")
            print(sThu)

            sFri = "The availabe airports on friday are "
            for i in SelfContainingClass.getfGraph().nodes:
                sFri += str(i.getName() + " " + i.getAbbreviation() + " ")
            print(sFri)

            sSat = "The availabe airports on saturday are "
            for i in SelfContainingClass.getsGraph().nodes:
                sSat += str(i.getName() + " " + i.getAbbreviation() + " ")
            print(sSat)

            sSun = "The availabe airports on sunday are "
            for i in SelfContainingClass.getuGraph().nodes:
                sSun += str(i.getName() + " " + i.getAbbreviation() + " ")
            print(sSun)

        except:
            pass
        SelfContainingClass.putGraph(map)
        SelfContainingClass.putmGraph(mon)
        SelfContainingClass.puttGraph(tue)
        SelfContainingClass.putwGraph(wed)
        SelfContainingClass.puthGraph(thu)
        SelfContainingClass.putfGraph(fri)
        SelfContainingClass.putsGraph(sat)
        SelfContainingClass.putuGraph(sun)


def getPath(path: list):
    total_price = 0
    total_duration = 0
    for i in range(len(path) - 1):
        origin = path[i]
        destination = path[i + 1]

        duration = SelfContainingClass.getGraph()[origin][destination]["duration"]
        price = SelfContainingClass.getGraph()[origin][destination]["price"]

        total_price += price
        total_duration += duration
        print("\t{} -> {}\n    - Duration: {} Price: {} €".format(str(path[i].getName()), str(path[i + 1].getName()),
                                                                  str(duration), str(price)))

    print("\n\t\tTotal Duration: {} Total price: {} € \n".format(total_duration, total_price))


def allPaths(dayNum, airP1: Airport, airP2: Airport, dayOfWeek):
    if dayNum == 0: day = SelfContainingClass.getGraph()
    if dayNum == 1: day = SelfContainingClass.getmGraph()
    if dayNum == 2: day = SelfContainingClass.gettGraph()
    if dayNum == 3: day = SelfContainingClass.getwGraph()
    if dayNum == 4: day = SelfContainingClass.gethGraph()
    if dayNum == 5: day = SelfContainingClass.getfGraph()
    if dayNum == 6: day = SelfContainingClass.getsGraph()
    if dayNum == 7: day = SelfContainingClass.getuGraph()

    try:
        print(
            dayOfWeek+" Journey from " + airP1.getName() + " (" + airP1.getAbbreviation() + ") to " + airP2.getName() + " (" + airP2.getAbbreviation() + ").")
        path = (nx.dijkstra_path(day, source=airP1, target=airP2, weight=None))
        print("     Less flight scales: \n")
        getPath(path)
        print("     Cheapest: \n")
        path = (nx.dijkstra_path(day, source=airP1, target=airP2, weight="price"))
        getPath(path)
        print("     Shortest: \n")
        path = (nx.dijkstra_path(day, source=airP1, target=airP2, weight="duration"))
        getPath(path)
    except Exception as e:
        print("     There is not a flight on " + dayOfWeek)
